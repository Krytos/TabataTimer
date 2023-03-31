import asyncio
import flet as ft


async def start_tabata_timer(event):
	page = event.page
	if page.timer_task is not None:
		page.timer_task.cancel()
	work_duration = int(page.work_duration_input.value)
	rest_duration = int(page.rest_duration_input.value)
	rounds = int(page.rounds_input.value)

	page.timer_task = asyncio.create_task(run_timer(page, work_duration, rest_duration, rounds))
	await page.timer_task


async def run_timer(page, work_duration, rest_duration, rounds):
	for cycle in range(1, rounds + 1):
		page.current_cycle_label.value = f"Round {cycle} / {rounds}"
		await page.update_async()

		for remaining in range(work_duration, -1, -1):
			page.timer_label.value = f"Work: {remaining}s"
			await page.update_async()
			await asyncio.sleep(1)

		for remaining in range(rest_duration, -1, -1):
			page.timer_label.value = f"Rest: {remaining}s"
			await page.update_async()
			await asyncio.sleep(1)

	page.timer_label.value = "Tabata Completed!"
	await page.update_async()


async def on_start_button_click(e):
	await start_tabata_timer(e)


async def on_reset_button_click(e):
	page = e.page
	page.timer_label.value = "Ready?"
	page.current_cycle_label.value = ""
	if page.timer_task is not None:
		page.timer_task.cancel()
	await page.update_async()

async def main(page: ft.Page):
	page.title = "Tabata Timer"
	page.window_width = 400
	page.window_height = 300
	page.window_resizable = False
	page.timer_task = None

	main_row = ft.Row(width=page.window_width, tight=True)
	timer_column = ft.Column(tight=False, width=page.window_width * 0.4)
	controls_column = ft.Column(tight=True, width=page.window_width * 0.6)

	page.work_duration_input = ft.TextField(
		autofocus=True, hint_text="Work Duration (s)", value="20", dense=True, width=page.window_width * 0.5
		)
	page.rest_duration_input = ft.TextField(
		autofocus=True, hint_text="Rest Duration (s)", value="10", dense=True, width=page.window_width * 0.5
		)
	page.rounds_input = ft.TextField(
		autofocus=True, hint_text="Rounds", value="8", dense=True, width=page.window_width * 0.5
		)

	start_button_content = ft.Text("Start", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)
	start_button = ft.Container(
		content=start_button_content, bgcolor=ft.colors.GREEN, on_click=on_start_button_click, width=100, height=50,
		alignment=ft.alignment.center, border_radius=10
		)

	reset_button_content = ft.Text("Reset", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD)
	reset_button = ft.Container(
		content=reset_button_content, bgcolor=ft.colors.RED, on_click=on_reset_button_click, width=100, height=50,
		alignment=ft.alignment.center, border_radius=10
		)

	page.timer_label = ft.Text(
		"Ready?", size=30, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_600
	)
	page.current_cycle_label = ft.Text(
		"", size=16, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.W_500, color=ft.colors.GREEN_700
	)

	button_row = ft.Row(
		tight=True, wrap=False, controls=[start_button, reset_button], alignment=ft.MainAxisAlignment.SPACE_EVENLY,
		width=page.window_width * 0.5
		)

	timer_column.controls = [page.timer_label, page.current_cycle_label]
	controls_column.controls = [page.work_duration_input, page.rest_duration_input, page.rounds_input, button_row]
	main_row.controls = [timer_column, controls_column]
	await page.add_async(main_row)
	await page.update_async()


if __name__ == "__main__":
	ft.app(target=main)
