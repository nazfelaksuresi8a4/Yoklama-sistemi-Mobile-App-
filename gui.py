import flet as ft 
import Router
import backend
from abc import ABC, abstractmethod


class RuleAbstraction(ABC):
    @abstractmethod
    def mainPage(self):
        pass
    
    @abstractmethod
    def loginPage(self):
        pass
    
    @abstractmethod
    def registerPage(self):
        pass

    @abstractmethod
    def mainMenu(self):
        pass

class mainWindow():
    def __init__(self):
        self.roots = Router.Roots()
        self.router = Router.RouterClass()
        self.BackendModule = backend.Backend()
        self.page = None

    def mainMenu(self,page : ft.Page):
        '''page-settings'''
        page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Sayfanın dikey ortalaması
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Sayfanın yatay ortalaması

        self.page = page
        self.controls = page.controls

        '''widget-styles'''
        self.textStyle = ft.TextStyle(size=24,
                                      font_family='arial',
                                      bgcolor=self.page.bgcolor,
                                      color=ft.Colors.WHITE_24)
        
        self.buttonStyle = ft.ButtonStyle(color=ft.Colors.WHITE_54,
                                          bgcolor=ft.Colors.ORANGE,
                                          elevation=24,
                                          shape=ft.RoundedRectangleBorder(radius=24),
                                          overlay_color={
                                                  ft.ControlState.HOVERED : ft.Colors.ORANGE_800,
                                                  ft.ControlState.PRESSED : ft.Colors.RED_600,
                                                  ft.ControlState.DEFAULT : ft.Colors.ORANGE
                                                        },
                                          shadow_color=ft.Colors.BLACK, 
                                          )


        '''widgets-login'''
        self.login_label = ft.Text(value='Giriş yapın',
                                   text_align=ft.TextAlign.CENTER,
                                   align=ft.Alignment.CENTER,
                                   style=self.textStyle,
                                   )

        self.login_status_label = ft.Text(value='Durum: Giriş yapılmadı',
                                   text_align=ft.TextAlign.CENTER,
                                   align=ft.Alignment.CENTER,
                                   style=self.textStyle)
        
        self.password_input = ft.TextField(hint_text='Şifrenizi girin',
                                           password=True,
                                           text_align=ft.TextAlign.CENTER,
                                           align=ft.Alignment.CENTER,
                                           text_style=self.textStyle,
                                           border_radius=24,
                                           border_color=ft.Colors.CYAN)
        
        self.gmail_input = ft.TextField(hint_text='Gmail adresinizi girin',
                                        text_align=ft.TextAlign.CENTER,
                                        align=ft.Alignment.CENTER,
                                        text_style=self.textStyle,
                                        border_radius=24,
                                        border_color=ft.Colors.CYAN)
        
        self.apply_login_button = ft.ElevatedButton(content='Giriş yap',
                                                    style=self.buttonStyle
                                                    )
        
        self.example_register_button = ft.TextButton(content='Hesabın yokmu Kayıt ol')


        '''widgets-register'''
        self.register_lbl = ft.Text(value='Kayıt ol',
                                    text_align=ft.TextAlign.CENTER,
                                    style=self.textStyle,
                                    align=ft.Alignment.CENTER)
        
        self.register_gmail_input = ft.TextField(hint_text='Gmail adresinizi girin',
                                                 text_align=ft.TextAlign.CENTER,
                                                 align=ft.Alignment.CENTER,
                                                 text_style=self.textStyle,
                                                 border_radius=24,
                                                 border_color=ft.Colors.CYAN)

        self.register_password_input = ft.TextField(hint_text='Şifrenizi girin',
                                                    text_align=ft.TextAlign.CENTER,
                                                    align=ft.Alignment.CENTER,
                                                    text_style=self.textStyle,
                                                    password=True,
                                                    border_radius=24,
                                                    border_color=ft.Colors.CYAN)
        
        self.register_button = ft.ElevatedButton(content='Kayıt ol',
                                                style=self.buttonStyle,
                                                elevation=0.35,
                                                align=ft.Alignment.CENTER)
        
        self.register_status_label = ft.Text(value='Durum: Kayıt olunmadı',
                                            text_align=ft.TextAlign.CENTER,
                                            style=self.textStyle,
                                            align=ft.Alignment.CENTER)
        
        self.example_login_button = ft.TextButton(content='Giriş ekranına geri dön')

        '''widget-lists'''
        self.login_widgets_list = [self.login_label,
                                  self.gmail_input,
                                  self.password_input,
                                  self.login_status_label,
                                  self.example_register_button,
                                  self.apply_login_button,]
        
        self.register_widgets_list = [self.register_lbl,
                                      self.register_gmail_input,
                                      self.register_password_input,
                                      self.register_status_label,
                                      self.example_login_button,
                                      self.register_button]
        
        '''object-dictionaries'''
        self.type_dict = {'page': type(page)}

        '''functions'''
        #Ui Functions
        self.routeLoginScreen = lambda _ : self.router.swapUi(self.page,
                                                              self.controls,
                                                              self.login_widgets_list,
                                                              self.type_dict)

        self.routeRegisterScreen = lambda _ : self.router.swapUi(self.page,
                                                              self.controls,
                                                              self.register_widgets_list,
                                                              self.type_dict)


        #Button-Functions
        self.example_register_button.on_click = self.routeRegisterScreen
        self.example_login_button.on_click = self.routeLoginScreen

        #Backend-Function-Connections
        self.apply_login_button.on_click = self.getLoginRequest

        '''function-calls'''
        self.uiSwap = self.routeLoginScreen('')
        
        page.update()

        print(f'uiSwap event returned: {self.uiSwap}')

    def getLoginRequest(self,_):
        self.gmail_value,self.password_value = self.gmail_input.value,self.password_input.value
        
        values = [self.gmail_value,self.password_value]
        c = [n for n in range(len(values)) if len(values[n]) > 4]
        
        if len(c) == 2:
            response = self.BackendModule.login(self.gmail_value,
                                                self.password_value)

            return response

        else:
            return 'Lütfen Şifre ve Gmail alanlarını doldurup tekrar deneyiniz!'


        

    def errorPage(self,page : ft.Page):
        controls = page.controls

        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER 

        page.add(ft.Text(value='Hata: Ana sayfa akışı yüklenemedi. Lütfen programı yeniden başlatıp tekrar deneyiniz',
                         color=ft.Colors.GREEN,
                         bgcolor=ft.Colors.RED_600))
        

    def getPage(self):
        if self.page is not None:
            return self.mainMenu
        
        else:
            return self.errorPage

windowThread = mainWindow()

ft.app(windowThread.mainMenu)
