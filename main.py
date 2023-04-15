import flet as ft

appName = "Deff Not Nun Shark"
class Task(ft.UserControl):
    def __init__(self, input_text, remove_task):
        super().__init__()
        self.input = input_text
        self.remove_task = remove_task

    def build(self):
        self.task_cb = ft.Checkbox(label=self.input,
                                   on_change=self.setOpacity,
                                   expand=True)
        self.edit_tf = ft.TextField(value=self.input,
                                    expand=True)
        self.edit_task = ft.IconButton(icon=ft.icons.CREATE_OUTLINED,
                              on_click=self.edit_clicked)
        self.del_task = ft.IconButton(icon=ft.icons.DELETE_OUTLINE,
                              on_click=self.remove_clicked)
        self.task_view = ft.Row(
            visible=True,
            controls=[
                self.task_cb,
                self.edit_task,
                self.del_task
            ]
        )

        self.edit_view = ft.Row(
            visible=False,
            controls=[
                self.edit_tf,
                ft.IconButton(icon=ft.icons.CHECK,
                              on_click=self.save_clicked)
            ]
        )

        return ft.Column(controls=[self.task_view, self.edit_view])

    def edit_clicked(self, _):
        self.edit_view.visible = True
        self.task_view.visible = False
        self.update()

    def remove_clicked(self, _):
        self.remove_task(self)

    def save_clicked(self, _):
        self.task_cb.label = self.edit_tf.value
        self.edit_view.visible = False
        self.task_view.visible = True
        self.update()

    def setOpacity(self, _):
        if self.task_cb.value == True:
            self.task_view.opacity = 0.4
            self.edit_task.disabled = True
            self.del_task.disabled = True
        else:
            self.task_view.opacity = 1
            self.edit_task.disabled = False
            self.del_task.disabled = False
        self.update()

class ToDo(ft.UserControl):
    def build(self):
        self.input = ft.TextField(hint_text="What should be done?",
                                  expand=True,
                                  autofocus=True)
        self.tasks = ft.Column()
        
        titleThingy = ft.Row(controls=[
                ft.Text(value=appName,
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINE)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls = [
                titleThingy,
                ft.Row(
                    controls=[
                        self.input,
                        ft.FloatingActionButton(icon=ft.icons.ADD,
                                                on_click=self.add_clicked)
                    ]
                ),
                self.tasks
            ]
        )
        return view
    
    def add_clicked(self, _):
        if self.input.value !="":
            task = Task(self.input.value, self.remove_task)
            self.input.value =""
            self.input.focus()
            self.tasks.controls.append(task)
            self.update()

    def remove_task(self, task):
        self.tasks.controls.remove(task)
        self.input.focus()
        self.update()

def main(page: ft.Page):
    page.window_height = 640
    page.window_width = 360
    page.title = appName
    todo = ToDo()
    page.add(todo)

ft.app(target=main)
