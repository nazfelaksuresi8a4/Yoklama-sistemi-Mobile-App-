class Roots:
    @property
    def login_screen(self):
        return '/login'

    @property
    def register_screen(self):
        return '/register'

    @property
    def mainmenu_screen(self):
        return '/mainmenu'


class RouterClass:
    
    @staticmethod
    def swapUi(page,controls,widgets,type_dict):
        if type(page) == type_dict['page'] and len(widgets) > 0:
            try:
                controls_history = controls.copy()
                controls.clear()

                for widget in widgets:
                    controls.append(widget)

                page.update()
                
            except Exception as ui_swap_exception:
                    return {'error': 'Ui swap excepiton',
                            'exception': {ui_swap_exception},
                            'status': 'Failed',
                            'controls-history': controls_history,
                            'current-history': controls.copy()}

            return {'error': None,
                    'exception': None,
                    'status': 'succesfuly',
                    'controls-history': controls_history,
                    'current-history': controls.copy()}

        else:
            return {'error': 'Page or widgets not found',
                    'exception': 'Not defined',
                    'status': 'Failed',
                    'controls-history': controls_history,
                    'current-history': controls.copy()}

        
