from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

#:set text_color get_color_from_hex("#4a4939")
#:set focus_color get_color_from_hex("#e7e4c0")
#:set ripple_color get_color_from_hex("#c5bdd2")
#:set bg_color get_color_from_hex("#f7f4e7")
#:set selected_color get_color_from_hex("#0c6c4d")


<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: focus_color
    unfocus_color: bg_color
    text_color: text_color
    icon_color: text_color
    ripple_color: ripple_color
    selected_color: selected_color


<DrawerLabelItem@MDNavigationDrawerItem>
    bg_color: bg_color
    text_color: text_color
    icon_color: text_color
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        ScreenManager:

            MDScreen:

                MDToolbar:
                    title: "BigCalculator"
                    elevation: 10
                    pos_hint: {"top": 1}
                    md_bg_color: focus_color
                    specific_text_color: text_color
                    left_action_items:
                        [                             [                             'menu', lambda x:                             nav_drawer.set_state("open")                             if nav_drawer.state == "close" else                             nav_drawer.set_state("close")                             ]                             ]
                Widget:

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0) if self.anchor == "left" else (16, 0, 0, 16)
            md_bg_color: bg_color

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Created by kilhh"
                    title_color: text_color
                    text: "Calculator"
                    title_color: text_color
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Calculator"

                DrawerClickableItem:
                    right_text: "+ - / *"
                    text_right_color: text_color
                    text: "OrdinaryCalculator"

                DrawerClickableItem:
                    text: "BMICalculator"
                    
                DrawerClickableItem:
                    text: "% Calculator"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "information"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "Who created it ?"

                DrawerLabelItem:
                    icon: "information-outline"
                    text: "When was the program created ?"
'''


class MortgagaCalculatorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_string(KV)


MortgagaCalculatorApp().run()