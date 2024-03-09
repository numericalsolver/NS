from flet import *
import flet as ft
from pages.landnding import landing_class as ls
from pages.components import components_class as cs
from pages.subjects import subjects_class as sc
from pages.dsp import  dsp_class as dspc

def main(page: Page):
    fonts={
    "inter":"fonts/Inter-VariableFont_slnt,wght.ttf",
    "impact":"fonts/impact.ttf",
    "calibri":"fonts/calibri-regular.ttf"
    }
      
    pages_v = {
        '/':View(
                    "/",
                    [
                    ls()
                    ],
                ),
        '/subjects':View(
                "/subjects",
                [
                    sc()
                ]
        ),
        '/subjects/dsp':View(
            "/subjects/dsp",
            [
            dspc()
            ]
        ),
        # '/create_task': View(
        #               "/create_task",
        #               [
        #                   create_task_view
        #               ],
        #           )

        }

    def route_change(route):
        page.views.clear()
        page.views.append(
        pages_v[page.route]
        )
        # if page.route =="/":
        #   page.update()
        #   time.sleep(1)
        #   page.go("/dashboard")



        # if page.route==f"/dashboard/subject/{subject}":
        #   if subject in subjects.values():
        #     page.update()
        #     page.go("/subjects/subjects")

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        page.update()


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




app(target=main,assets_dir='assets', port=5000)