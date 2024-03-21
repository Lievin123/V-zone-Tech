import flet as ft
from flet import *
import datetime as dt

def main (page : ft.Page):
    page.title = "v-zone Tech"
    page.bgcolor = ft.colors.BLUE_100
    page.padding = 7
    logo_i = Image("vzon.png",expand = True,top = 0,right = 0,height = 80)
    
    def format_ev(e :ControlEvent)-> None:
        page.clean()
        page.bgcolor = ft.colors.BLUE_800
        current_time = dt.datetime.now().time().strftime("%H:%M:%S.%f")
        current_date = dt.datetime.now().strftime("%Y-%m-%d")
        time_text = current_time 
        
        
        
        
        
        rti_text = Text('V_zone Code Academy',weight = 'bold',color ='#CDF5FD',bottom = 20,size = 28, left= 4 )
        bar_lat = Container(
            expand = True,
            bgcolor = ft.colors.BLUE_800,
            height = 120,
            right = 0,
            left = 0,
            content = Stack(expand = True,controls=[menu,rti_text])
        )
        heure_ui = Text(time_text,size = 50,weight = 'bold',top = 0,color = ft.colors.LIGHT_BLUE_50)          
        photo_cours = Container(
            expand= True,
            bgcolor = 'black',
            top = 0,
            height = 105,
            right = 0,
            left= 0,
            border_radius = 10,
            
            content =Stack(expand = True,controls =[
                Image(src ='cours.jpg',expand = True,color = ft.colors.TRANSPARENT),
                heure_ui,            
                Text(current_date,size = 20,weight = 'bold',bottom = 10 ,right = 5,color = ft.colors.LIGHT_BLUE_50,)
                ])       
        )
        
        #ici nous allons établir les événement
        
        
        
            
            


        question_text = Text("Formations en ligne",color = ft.colors.BLUE_800,weight = 'bold',size = 17,bottom =25 ,)

        
        question = ElevatedButton(
            right = 10,
            left = 10,
            top = 0,
            height = 110,
            width = 110,
            on_click = lambda e: page.launch_url("https://meet.google.com/tjm-ncpe-gsj"),
            
            content = Image(src='form.png',expand = True,width = 100,height = 100),
                )
        administrator_sys = Container(
            expand= True,
            bgcolor = '#CDF5FD',
            height= 135,
            bottom = 100,
            right = 50,
            left= 50,
            border_radius = 10,
            shadow = [
                    ft.BoxShadow(
                        offset = ft.Offset(20, -20),
                        blur_radius = 60,
                        color = "#DCEDC8",
                        blur_style = ft.ShadowBlurStyle.NORMAL,
                    ),
                    ft.BoxShadow(
                        offset = ft.Offset(-20, 20),
                        blur_radius = 60,
                        color = "black",
                        blur_style = ft.ShadowBlurStyle.NORMAL,
                    ),
                ],
            content = Stack(expand = True, controls = [question,])
            )
        


        
        bar_cours = Container(
            expand= True,
            bgcolor = '#CDF5FD',
            top = 120,
            bottom = 15,
            right = 00,
            left= 0,
            border_radius = 10,
            
            shadow = [
                    ft.BoxShadow(
                        offset = ft.Offset(20, -20),
                        blur_radius = 60,
                        color = "#DCEDC8",
                        blur_style = ft.ShadowBlurStyle.NORMAL,
                    ),
                    ft.BoxShadow(
                        offset = ft.Offset(-20, 20),
                        blur_radius = 60,
                        color = "black",
                        blur_style = ft.ShadowBlurStyle.NORMAL,
                    ),
                ],
            content=Stack(expand = True,controls = [photo_cours, administrator_sys,remise])
        )
        cam = Container(
            expand=True,
            bgcolor = ft.colors.BLUE_800,
            content=Stack(expand = True,controls = [bar_lat,bar_cours])      
        )
        page.add(cam)
        while True :
            heure_ui.value == dt.datetime.now().time().strftime("%H:%M:%S")
            heure_ui.update()
            

    vzn = Container(
        expand = True,
        height = 190,
        top = 45,
        width = 200,
        right = 0,
        left = 0,
        border_radius = 10,
        padding = -10,
        bgcolor= 'black',
        
        
        content = Image(src="vzone.jpg" ,expand = True)
    )
    text_vzn = Text(value = "V_zone propose",weight = 'bold',color = '#ECF4D6',size = 25,text_align = 'CENTER')
    services =Text("– expert mecanicien ",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    archi =Text("– architecture moderne",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    info =Text("– assistance informatique",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    dev =Text("– developpeur full stack",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    archin =Text("– architecture de l'interieur",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    deco =Text("– organisation evenementielle ",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    marque =Text("– marketing digital",text_align = 'CENTER',color = '#ECF4D6',size = 18)
    com =Text("– commission des biens ",size = 18,text_align = 'CENTER',color = '#ECF4D6')
    co =Text(" Services V-zone",size = 12,text_align = 'CENTER',color = 'white')
    bouton_cont = ElevatedButton(text = "Nous contacter",color = 'white',height = 30,bgcolor= 'blue',width = 150,right = 10,top = 2 , on_click = lambda e:page.launch_url(" https://wa.me/qr/5GLGY7X7MSGDP1 "))
    remise = ElevatedButton(text = "remise des TPS ",color = 'white',height = 30,bgcolor= 'blue',width = 150,right = 10,bottom = 2 , on_click = lambda e: page.launch_url("https://4p6jn8m6.forms.app/remise-des-travaux-pratiques-v-zone-code-academy"))
    
    pagina = Container(
        expand = True,
        top = 200,
        width = 200,
        height = 400,
        right = 10,
        left = 10,
        border_radius = 10,
        padding = 10,
        gradient = LinearGradient(
            begin = alignment.bottom_left,
            end = alignment.top_right,
            colors =('#9EC8B9','#5C8374'),
        ),
        shadow = [
                ft.BoxShadow(
                    offset = ft.Offset(20, -20),
                    blur_radius = 60,
                    color = "#DCEDC8",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
                ft.BoxShadow(
                    offset = ft.Offset(-20, 20),
                    blur_radius = 60,
                    color = "black",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                    ),
                ],
        content =(
            Row (
                controls = [
                    Column(
                        [text_vzn,
                         services,
                         archi,
                         info,
                         dev,
                         archin,
                         deco,
                         marque,
                         com,
                        ]
                    )
                ],
                alignment = ft.MainAxisAlignment.CENTER
            )

        )
    )
    def boutique_event(e :ControlEvent)->None:
        btk = Container(
            expand =True,
            bgcolor='#FBFADA',
            content= Stack(expand =True,controls =[vzn,pagina,bouton_cont,menu,h1])
        )
        page.clean()
        page.add(btk)

    vzone =CupertinoButton (
        width = 300 ,
        height = 300,
        on_click = boutique_event,
        content=Image("serv_v.png",expand = True)
        
    )
    dlg = ft.AlertDialog(
        title =ft.Text("V-zone Code Academy ",weight ='bold'),
        content = ft.Text("soyez sûr d'être informé sur l'heure de la formation",color = 'red'),
        actions=[
            ft.TextButton("suivre la formation", on_click= lambda e:page.launch_url("https://meet.google.com/tjm-ncpe-gsj")),
            ft.TextButton("remettre un TP", on_click= lambda e:page.launch_url("https://4p6jn8m6.forms.app/remise-des-travaux-pratiques-v-zone-code-academy")),
        ],
        

        )
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    dlge = ft.AlertDialog(
        title =ft.Text("V-zone web shop",weight ='bold'),
        content = ft.Text("temporairement indisponible",color = 'red'),
        
        

        )
    def open_dlge(e):
        page.dialog = dlge
        dlge.open = True
        page.update()
        

    vzone_boutique =CupertinoButton (
        width = 200 ,
        height = 200,
        on_click = open_dlge ,
        content=Image("bout.png",expand = True)
        
    )
    

    formation =CupertinoButton (
        width = 250 ,
        height = 250,
        on_click = open_dlg,
        content=Image("form.png",expand = True)
        
    )
    def hh_e (e :ControlEvent)-> None:
        
        page.clean()
        page.add(c)
    h1 = Container(
            expand = True,
            height = 45,
            bottom = 10,
            width = 45,
            left = 20,
            padding = -25,
            border_radius = 10,
            bgcolor = '#33691E',
            content = ElevatedButton(
                content=Image(src = "hom.jpg"),
                on_click = hh_e
            )
        )


    menu = Container (
        expand = True,
        height = 45,
        width = 60,
        top = 0,
        left = 0,
        border_radius = 10,
        content = PopupMenuButton(
            content = Image(src = "menu.png"),
            items =[
                ft.PopupMenuItem(text = 'Fermer'),
                ft.PopupMenuItem(
                    content = ft.Row([
                        ft.Icon(ft.icons.HOURGLASS_TOP_OUTLINED),
                        ft.Text("Service Client")
                    ]),
                    on_click = lambda e: page.launch_url('mailto: vzonetech800@gmail.com' )
                ),
                ft.PopupMenuItem(),
                ft.PopupMenuItem(
                    text = "A propos de V_zone Class",checked = True , on_click = lambda e:page.launch_url("https://sites.google.com/view/v-zonetech/accueil")
                )
            ]
        )
    )
    

    presentation =Container(
        bgcolor = ft.colors.BLUE_800,
        left = 0,
        opacity = 80,
        height = 500,
        right = 0,
        top= 80,
        content =Stack(controls =[
            Image("dev.jpg",expand = True,top = 0,width = 700, right = 0,left = 0 ),
            Text("Bienvenue sur ",weight = "bold",color = ft.colors.BLUE_100,left = 5,size = 25,top = 5),
            Text("V-zone Tech",weight = "bold",color = ft.colors.BLUE_100,left = 20,size = 30,top = 45),
            Text("\"La zone des visions technologiques\" ",weight = "bold",color = ft.colors.BLUE_100,left = 50,size = 12,top = 95,),
            Image("swimp.png",top = 210,height = 15,width = 70,),
            Container(
                left = 10,
                right = 10,
                bottom = 100,
                bgcolor = ft.colors.BLUE_100,
                top =200,
                shadow = [
                ft.BoxShadow(
                    offset = ft.Offset(20, -20),
                    blur_radius = 60,
                    color = "#DCEDC8",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
                ft.BoxShadow(
                    offset = ft.Offset(-20, 20),
                    blur_radius = 60,
                    color = "black",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
            ],
                content =(
                    Column (
                        controls = [
                            Row(
                                [vzone,
                                 formation,
                                 vzone_boutique
                                ],
                            scroll = ft.ScrollMode.AUTO,
                            )
                        ],
                        alignment = ft.MainAxisAlignment.CENTER
                    )
                )
            )
            ,
        ]
        ),
        shadow = [
                ft.BoxShadow(
                    offset = ft.Offset(20, -20),
                    blur_radius = 60,
                    color = "#DCEDC8",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
                ft.BoxShadow(
                    offset = ft.Offset(-20, 20),
                    blur_radius = 60,
                    color = "black",
                    blur_style = ft.ShadowBlurStyle.NORMAL,
                ),
            ],
        
        )
    
    

    c = Container(
        expand = True,
        bgcolor = ft.colors.BLUE_100 ,
        content=Stack(controls = [presentation,logo_i,menu,])      
    )
    page.add(c)
    

if __name__ =="__main__":
    ft.app(target = main,assets_dir = "assets")