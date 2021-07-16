import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gdk

import os

cwd = "/usr/share/applications"
dire = os.listdir(cwd)
l = []
for y in dire:
    indice = []    
    if os.path.isdir('/usr/share/applications/'+y)==False:
        text = open('/usr/share/applications/'+y)

        for x in text:

            val = x.split()
            
            if len(val)!=0 and len(indice)<2:
                if val[0][:5] == "Name=":
                    indice.append(val[0])
                if val[0][:5] == "Icon=" and len(indice)!=0:
                    indice.append(val[0])
                    
        
        if indice !=None:
            l.append(indice)
        text.close()


ui = Gtk.Builder()
ui.add_from_file("principal.glade")




class carregar_categorias():

    pass

class ListaCategoriaRow(Gtk.ListBoxRow):

    def __init__(self,  page_name, icon_name):
        Gtk.ListBoxRow.__init__(self)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box.set_border_width(6)
        image = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.BUTTON)
        box.pack_start(image, False, False, 0)
        label = Gtk.Label()
        label.set_text(page_name)
        box.pack_start(label, False, False, 0)
        self.add(box)


class ListaAppRow(Gtk.ListBoxRow):

    def __init__(self,  page_name, icon_name):
        Gtk.ListBoxRow.__init__(self)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box.set_border_width(6)
        image = Gtk.Image.new_from_icon_name(icon_name, Gtk.IconSize.BUTTON)
        box.pack_start(image, False, False, 0)
        label = Gtk.Label()
        label.set_text(page_name)
        box.pack_start(label, False, False, 0)
        self.add(box)

class Handler(object):
    def __init__(self, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)

        lista_box = ui.get_object("lista_aplicativos")
        list_box = ui.get_object("lista_categoria")
        
        list_box.add(ListaCategoriaRow(("Todos"), "emblem-favorite" ))

        list_box.add(ListaCategoriaRow(("First Steps"), "dialog-information" ))
        list_box.add(ListaCategoriaRow(("Welcome"), "rhythmbox" ))

        
        for x in l:
            if len(x) != 0: 
                nome = x[0].replace("Name=","")
                
                if len(x)>1 :
                    icon = x[1].replace("Icon=","")
                else:
                    icon = " "


                lista_box.add(ListaAppRow((nome), icon ))
            
        

    
    def app_selecionado(self,lista_box, row):

        menu_btn = ui.get_object("botaos")
        controle = ui.get_object("controle")
        
        remove = controle.get_children()
        print(remove)

        controle.remove(remove[0])
        
        controle.add(menu_btn)
        

    def categoria_selecionado(self, lista_box, row):

        print("ora ora")
        print(lista_box)
        print(row)

        pass

    def iniciar(self, *args):
        print("asd")
        print(self.lista_categoria)


    def onDestroy(self, *args):
        Gtk.main_quit()        




        

ui.connect_signals(Handler())

window = ui.get_object("principal")
window.show_all()

Gtk.main()

