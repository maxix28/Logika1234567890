from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import json
app = QApplication([])

def writeToFile():
    with open('notes.json','w',encoding='utf8') as file:
        json.dump(notes, file,ensure_ascii=False, sort_keys=True,indent=4)

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)
    

'''Інтерфейс програми'''
# параметри вікна програми
notes_win = QWidget()
#notes_win.setWindowTitle('Розумні замітки')
notes_win.resize(900, 600)


# віджети вікна програми
list_notes = QListWidget()
#list_notes_label = QLabel('Список заміток')


button_note_create = QPushButton('Створити замітку') # з'являється вікно з полем "Введіть ім'я замітки"
button_note_del = QPushButton('Видалити замітку')
button_note_save = QPushButton('Зберегти замітку')
#ield_tag = QLineEdit('')
#field_tag.setPlaceholderText('Введіть тег...')
field_text = QTextEdit()
#button_tag_add = QPushButton('Додати до замітки')
#button_tag_del = QPushButton('Відкріпити від замітки')
#button_tag_search = QPushButton('Шукати замітки по тегу')
#list_tags = QListWidget()
#list_tags_label = QLabel('Список тегів')
# розташування віджетів по лейаутах
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
col_2 = QVBoxLayout()
#col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)
col_2.addLayout(row_1)
col_2.addLayout(row_2)
# col_2.addWidget(list_tags_label)
# col_2.addWidget(list_tags)
# col_2.addWidget(field_tag)
# row_3 = QHBoxLayout()
# row_3.addWidget(button_tag_add)
# row_3.addWidget(button_tag_del)
# row_4 = QHBoxLayout()
# row_4.addWidget(button_tag_search)
# col_2.addLayout(row_3)
# col_2.addLayout(row_4)
layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

def exitt():
    app.exit()

def show_notes():
    global key
    key = list_notes.selectedItems()[0].text()
    
   # list_tags.clear()
    field_text.setText(notes[key]['текст'])
    
   # list_tags.addItems(notes[key]['теги'])


def delete_notes():
     if list_notes.currentItem():
         if key in notes:
             notes.pop(key)
            
             field_text.clear()
             #list_tags.clear()
             list_notes.clear()
             list_notes.addItems(notes)
            # writeToFile()

def save_notes():
    
     if list_notes.currentItem():
         key = list_notes.currentItem().text()
         notes[key]['текст'] = field_text.toPlainText()
         writeToFile()


def delete_notes():
     if list_notes.currentItem():
         if key in notes:
             notes.pop(key)
            
             field_text.clear()
             #list_tags.clear()
             list_notes.clear()
             list_notes.addItems(notes)
             writeToFile()

def add_notes():
     note_name,ok = QInputDialog.getText(notes_win,'Додати замітку',"Назва замітки")
     if note_name and ok:
         list_notes.addItem(note_name)
         notes[note_name] = {"текст":"","теги":[]}
     writeToFile()         

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

list_notes.addItems(notes)
button_note_save.clicked.connect(save_notes)
button_note_create.clicked.connect(add_notes)
list_notes.itemClicked.connect(show_notes)
button_note_del.clicked.connect(delete_notes)
# запуск програми
notes_win.show()
app.exec_()
