import json
import os
import re
import time
import sys, csv
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.ui_main_window import Ui_MainWindow
from ui.ui_customdictmanager_dialog import Ui_Dialog_CustomDictManager
from ui.ui_customdictinput_dialog import Ui_DialogCustomDictInput

APP_ICON = './assets/icon.png'
APP_DICT = './assets/dict.csv'
APP_DICT_CUSTOM = './assets/custom.json'

dict_all = []
dict_index = {}
search_text = ''
search_result = []


class MainWindowSignal(QObject):
    update_loadprogress = Signal(str)
    finish_loadprogress = Signal()
    finish_search = Signal()
    change_customdict = Signal()


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(APP_ICON))
        self.sig = MainWindowSignal()
        self.sig.update_loadprogress.connect(self.handle_update_loadprogress)
        self.sig.finish_loadprogress.connect(self.handle_finish_loadprogress)
        self.sig.finish_search.connect(self.refresh_list)
        self.sig.change_customdict.connect(self.load_data)
        self.ui.btn_search.clicked.connect(self.handle_search)
        self.ui.btn_opencustomdictmanager.clicked.connect(self.open_customdictmanager)
        self.ui.edit_search.textChanged.connect(self.handle_search)
        self.ui.list_search.currentItemChanged.connect(self.handle_click_item)
        self.ui.edit_search.setValidator(QRegularExpressionValidator('^[a-z]{0,30}$'))

        self.load_data()

    def load_data(self):
        global dict_all, dict_index

        dict_all = []
        dict_index = {}
        self.ui.btn_search.setDisabled(True)
        self.ui.edit_search.setDisabled(True)
        self.th = ThreadLoadData(self.sig.update_loadprogress)
        self.th.start()
        self.th.finished.connect(self.sig.finish_loadprogress)

    def handle_update_loadprogress(self, text: str):
        self.ui.label_status.setText(text)

    def handle_finish_loadprogress(self):
        self.ui.label_status.setText(f'词典加载完毕，共 {len(dict_all)} 条数据')
        self.ui.btn_search.setDisabled(False)
        self.ui.edit_search.setDisabled(False)

    def handle_search(self):
        global search_text

        search_text = self.ui.edit_search.text()
        if (hasattr(self, 'st')):
            if (self.st.isRunning()):
                self.st.terminate()
        self.st = ThreadSearch(self.sig.finish_search, self.ui.option_enablefuzzysearch.isChecked())
        self.st.start()

    def handle_click_item(self):
        try:
            data = dict_all[search_result[self.ui.list_search.currentIndex().row()]]
            self.ui.label_word.setText(data['word'])
            text = ''
            if (data['tag'] != ''):
                text += '标签：' + data['tag'].replace('zk', '中考').replace('gk', '高考').replace('ky', '考研').replace(
                    'ielts', '雅思').replace('toefl', '托福').upper() + '\n\n'
            if (data['translation'] != ''):
                text += '释义（中）：\n' + data['translation'].replace('\\n', '\n').replace('\\r', '') + '\n\n'
            if (data['definition'] != ''):
                text += '释义（英）：\n' + data['definition'].replace('\\n', '\n').replace('\\r', '') + '\n\n'
            self.ui.text_definition.setText(text)
        except:
            pass

    def refresh_list(self):
        self.ui.list_search.clear()
        e = False
        for item in search_result:
            e = True
            data = dict_all[item]
            self.ui.list_search.addItem(data['word'] + ' ' + data['translation'].replace('\\n', ' '))
        if e:
            self.ui.list_search.setCurrentRow(0)

    def open_customdictmanager(self):
        dialog = DialogCustomDictManager(self, self.sig.change_customdict)
        dialog.show()


class DialogCustomDictManagerSignal(QObject):
    item_add = Signal(str, str)
    item_change = Signal(str, str)


class DialogCustomDictManager(QDialog):

    def __init__(self, parent, signal) -> None:
        super().__init__(parent)
        self.ui = Ui_Dialog_CustomDictManager()
        self.ui.setupUi(self)

        self.signal = signal

        self.sig = DialogCustomDictManagerSignal()
        self.sig.item_add.connect(self.item_add)
        self.sig.item_change.connect(self.item_change)

        self.data_change = False

        self.ui.btn_save.clicked.connect(self.btnclick_save)
        self.ui.btn_add.clicked.connect(self.btnclick_add)
        self.ui.btn_del.clicked.connect(self.btnclick_del)
        self.ui.btn_edit.clicked.connect(self.btnclick_edit)

        if not os.path.exists(APP_DICT_CUSTOM):
            with open(APP_DICT_CUSTOM, 'w') as f:
                f.write('[]')
        with open(APP_DICT_CUSTOM) as f:
            try:
                self.word_list = json.loads(f.read())
            except:
                self.word_list = []
        self.refresh_list()

    def btnclick_save(self):
        self.data_change = True
        with open(APP_DICT_CUSTOM,'w') as f:
            f.write(json.dumps(self.word_list))

    def btnclick_add(self):
        dialog = DialogCustomDictInput(self, self.sig.item_add)
        dialog.show()

    def btnclick_del(self):
        if (self.ui.listWidget.currentIndex().row() >= 0):
            self.word_list.pop(self.ui.listWidget.currentIndex().row())
            self.ui.listWidget.removeItemWidget(self.ui.listWidget.takeItem(self.ui.listWidget.currentIndex().row()))

    def btnclick_edit(self):
        if (self.ui.listWidget.currentIndex().row() >= 0):
            data = self.word_list[self.ui.listWidget.currentRow()]
            dialog = DialogCustomDictInput(self, self.sig.item_change, data['word'], data['translation'])
            dialog.show()

    def item_add(self, word, defini):
        self.word_list.append({'word': word, 'translation': defini})
        self.ui.listWidget.addItem(f'{word}  {defini}')

    def item_change(self, word, defini):
        self.word_list[self.ui.listWidget.currentIndex().row()] = {'word': word, 'translation': defini}
        self.ui.listWidget.currentItem().setText(word + ' ' + defini)

    def refresh_list(self):
        self.ui.listWidget.clear()
        for item in self.word_list:
            self.ui.listWidget.addItem(f'{item["word"]}  {item["translation"]}')

    def closeEvent(self, event):
        if self.data_change:
            self.signal.emit()
        event.accept()


class DialogCustomDictInput(QDialog):

    def __init__(self, parent, signal, word='', defin='') -> None:
        super().__init__(parent)
        self.ui = Ui_DialogCustomDictInput()
        self.ui.setupUi(self)

        self.signal = signal

        self.ui.lineEdit.setText(word)
        self.ui.textEdit.setText(defin)

        self.ui.btn_y.clicked.connect(self.btnclick_y)
        self.ui.btn_n.clicked.connect(self.btnclick_n)

    def btnclick_y(self):
        self.signal.emit(self.ui.lineEdit.text(), self.ui.textEdit.toPlainText().replace('\n','\\n'))
        self.close()

    def btnclick_n(self):
        self.close()


class ThreadSearch(QThread):

    def __init__(self, signal, fuzzy) -> None:
        super().__init__()
        self.signal = signal
        self.fuzzy = fuzzy

    def run(self):
        global search_result

        # 优化连续输入相应
        time.sleep(0.3)
        if (search_text == ''):
            return
        result = []
        pattern_front = search_text + '(.*?)'
        pattern_fuzzy = '(.*?)' + '(.*?)'.join(list(search_text)) + '(.*?)'

        # 精确匹配
        if (dict_index.get(search_text)):
            result.append(dict_index.get(search_text))

        # 前缀匹配
        for item in dict_index.keys():
            if re.match(pattern_front, item):
                if (result.count(dict_index.get(item)) > 0):
                    continue
                result.append(dict_index.get(item))
                if (len(result) >= 40):
                    search_result = result
                    self.signal.emit()
                    return

        # 重合匹配
        for item in dict_index.keys():
            if item.find(search_text) != -1:
                if (result.count(dict_index.get(item)) > 0):
                    continue
                result.append(dict_index.get(item))
                if (len(result) >= 40):
                    search_result = result
                    self.signal.emit()
                    return

        if not self.fuzzy:
            search_result = result
            self.signal.emit()
            return

        # 模糊匹配
        for item in dict_index.keys():
            if re.match(pattern_fuzzy, item):
                if (result.count(dict_index.get(item)) > 0):
                    continue
                result.append(dict_index.get(item))
                if (len(result) >= 40):
                    search_result = result
                    self.signal.emit()
                    return

        search_result = result
        self.signal.emit()


class ThreadLoadData(QThread):

    def __init__(self, signal) -> None:
        super().__init__()
        self.signal = signal

    def run(self) -> None:
        global dict_all,dict_index
        custom_data = []
        # 加载自定义词典数据
        if os.path.exists(APP_DICT_CUSTOM):
            with open(APP_DICT_CUSTOM) as f:
                try:
                    custom_data = json.loads(f.read())
                except:
                    pass
        for item in custom_data:
            dict_all.append({'word': item['word'], 'definition': '', 'translation': item['translation'], 'tag': ''})
        # 加载词典数据
        with open(APP_DICT, encoding='utf-8') as f:
            reader = csv.reader(f)
            count = 0
            for item in reader:
                dict_all.append({'word': item[0], 'definition': item[2], 'translation': item[3], 'tag': item[7]})
                count += 1
                if (count >= 1024):
                    self.signal.emit(f'词典加载中，已加载 {len(dict_all)} 条数据')
                    count = 0

        self.signal.emit(f'建立索引中，请耐心等待……')
        dict_index = dict(
            zip([x['word'].lower().replace('-', '').replace(' ', '') for x in dict_all], range(len(dict_all))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())