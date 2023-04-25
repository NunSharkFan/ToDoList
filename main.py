import flet as ft

class task(ft.UserControl):
    def __init__(self, input_text, remove_task):
        super().__init__()
        self.remove_task = remove_task
        self.input = input_text

    def build(self):
        self.task_cb = ft.Checkbox(label=self.input,
                                   on_change=self.setOpacity,
                                   expand=True)
        self.edit_tf = ft.TextField(value=self.input,
                                    expand=True)
        self.edit_task = ft.IconButton(icon=ft.icons.CREATE_OUTLINED,
                              on_click=self.edit_clicked)
        self.del_task = ft.IconButton(icon=ft.icons.DELETE_OUTLINE,
                              on_click=self.confirm_remove)
        self.del_confirm = ft.Row(
            visible=False,
            controls=[
                ft.Text("Delete Task", expand=True),
                ft.FilledButton(text='Yes', on_click=self.remove_clicked),
                ft.FilledButton(text='No', on_click = self.exit_remove)
            ]
        )
        
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

        return ft.Column(controls=[self.task_view, self.edit_view, self.del_confirm])

    def exit_remove(self, _):
        self.task_view.visible = True
        self.del_confirm.visible = False
        self.update()

    def confirm_remove(self, _):
        self.task_view.visible = False
        self.del_confirm.visible = True
        self.update()

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

def main(page: ft.Page):
    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            page.update()
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.update()

    def del_task(task):
        tasks.controls.remove(task)
        page.update()


    def add_task(_):
        if inputThingy.value == '':
            return
        todo = task(inputThingy.value, del_task)
        tasks.controls.append(todo)
        inputThingy.value = ''
        page.update()
    
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 640
    page.window_width = 360
    page.title = "Deff Not Stolen"
    titleThingy = ft.Row(controls=[
                ft.Text(value="Deff Not Stolen",
                        style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINE, on_click=change_theme)],
                alignment=ft.MainAxisAlignment.CENTER
            )
    
    inputThingy = ft.TextField(label='Add Task', width= 280, height=50)

    taskAdderThingy = ft.Row(controls=[
                            inputThingy,
                            ft.FloatingActionButton(icon = ft.icons.ADD, width=50, height=50, on_click=add_task)])

    tasks = ft.ListView()

    view = ft.Column(controls=[
                        titleThingy,
                        taskAdderThingy,
                        tasks],

        )

    page.add(view)

ft.app(target=main)
