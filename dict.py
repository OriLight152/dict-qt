import re
import time
import sys, csv
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui.ui_main_window import Ui_MainWindow

dict_all = []
dict_index = {}
search_text = ''
search_result = []


class MainWindowSignal(QObject):
    update_loadprogress = Signal(str)
    finish_loadprogress = Signal()
    finish_search = Signal()


class MainWindow(QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(f'./assets/icon.png'))
        self.sig = MainWindowSignal()
        self.sig.update_loadprogress.connect(self.handle_update_loadprogress)
        self.sig.finish_loadprogress.connect(self.handle_finish_loadprogress)
        self.sig.finish_search.connect(self.refresh_list)
        self.ui.btn_search.clicked.connect(self.handle_search)
        self.ui.edit_search.textChanged.connect(self.handle_search)
        self.ui.list_search.currentItemChanged.connect(self.handle_click_item)
        self.ui.edit_search.setValidator(QRegularExpressionValidator('^[a-z]{0,30}$'))
        self.ui.btn_search.setDisabled(True)
        self.ui.edit_search.setDisabled(True)

        self.load_data()

    def load_data(self):
        self.th = LoadDataThread(self.sig.update_loadprogress)
        self.th.start()
        self.th.finished.connect(self.sig.finish_loadprogress)

    def handle_update_loadprogress(self, text: str):
        self.ui.label_status.setText(text)

    def handle_finish_loadprogress(self):
        global dict_all, dict_index
        self.ui.label_status.setText(f'词典加载完毕，共 {len(dict_all)} 条数据')
        dict_index = dict(
            zip([x['word'].lower().replace('-', '').replace(' ', '') for x in dict_all], range(len(dict_all))))
        self.ui.btn_search.setDisabled(False)
        self.ui.edit_search.setDisabled(False)

    def handle_search(self):
        global search_text

        print('handle search')
        # if (self.ui.edit_search.text() == search_text):
        #     return
        search_text = self.ui.edit_search.text()
        if (hasattr(self, 'st')):
            if (self.st.isRunning()):
                self.st.terminate()
        self.st = SearchThread(self.sig.finish_search, self.ui.option_enablefuzzysearch.isChecked())
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
            # self.ui.label_translation.setText(text)
            self.ui.text_definition.setText(text)
        except:
            pass

    def refresh_list(self):
        self.ui.list_search.clear()
        e = False
        for item in search_result:
            e=True
            data = dict_all[item]
            self.ui.list_search.addItem(data['word'] + ' ' + data['translation'].replace('\\n', ' '))
        if e:
            self.ui.list_search.setCurrentRow(0)


class SearchThread(QThread):

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


class LoadDataThread(QThread):

    def __init__(self, signal) -> None:
        super().__init__()
        self.signal = signal

    def run(self) -> None:
        time_start = time.time()
        with open('./assets/dict.csv', encoding='utf-8') as f:
            reader = csv.reader(f)
            count = 0
            for item in reader:
                dict_all.append({'word': item[0], 'definition': item[2], 'translation': item[3], 'tag': item[7]})
                count += 1
                if (count >= 1024):
                    self.signal.emit(f'词典加载中，已加载 {len(dict_all)} 条数据')
                    count = 0
        time_end = time.time()
        print(f'载入耗时：{time_end-time_start}秒')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())