import asyncio
from nicegui import app, ui


async def reset():
    start_button.text = "Start"
    minute_label.set_text("00:")
    second_label.set_text("00")
    milis_label.set_text(".0")
    round_label.set_text(f"Rounds: 0 / {rounds.value}")


async def countdown(t, type):
    for i in range(t - 1, -1, -1):
        if start_button.text == "Start":
            return
        if i == 50:
            ui.audio("countdown.wav", autoplay=True, controls=False)
        if i == 10 and type == "rest":
            ui.audio("work.mp3", autoplay=True, controls=False)
        minute_label.set_text(f"{i//600:02d}:")
        second_label.set_text(f"{i//10:02d}")
        milis_label.set_text(f".{i%10}")
        ui.update()
        await asyncio.sleep(0.1)


async def main():
    if start_button.text == "Start":
        start_button.text = "Stop"
        while True:
            w = int(work_time.value) * 10
            r = int(rest_time.value) * 10
            ro = int(rounds.value)
            for round in range(1, ro + 1):
                if start_button.text == "Start":
                    break
                round_label.set_text(f"Rounds: {round} / {ro}")
                await countdown(w, "work")
                await countdown(r, "rest")
                if round == ro:
                    ui.audio("done.mp3", autoplay=True, controls=False)
            await reset()
            break
    else:
        start_button.text = "Start"


with ui.column().style("align-items: center; justify-content: center;"):
    with ui.row().style("align-items: stretch; justify-content: center;"):
        minute_label = ui.label("00:")
        minute_label.style("font-size: 750%; font-weight: bold")
        second_label = ui.label("00")
        second_label.style("font-size: 750%; font-weight: bold; margin-left: -5%")
        milis_label = ui.label(".0")
        milis_label.style(
            "font-size: 350%; font-weight: bold; align-self: end; margin-bottom: 7%; margin-left: -5%"
        )
    round_label = ui.label().style("font-size: 250%; font-weight: bold")
    work_time = ui.input(label="Work", placeholder="20", value="20")
    work_time.props('input-style="font-size: 150%; width: 80%; text-align: right; "')
    rest_time = ui.input(label="Rest", placeholder="10", value="10")
    rest_time.props('input-style="font-size: 150%; width: 80%; text-align: right"')
    rounds = ui.input(label="Rounds", placeholder="8", value="8")
    rounds.props('input-style="font-size: 150%; width: 80%; text-align: right"')
    round_label.set_text(f"Rounds: 0 / {rounds.value}")
    start_button = ui.button("Start", on_click=lambda: main())
    start_button.style("width: 80%; height: 80%")


app.native.window_args["resizable"] = False
# app.native.start_args['debug'] = True
ui.run(native=True, window_size=(400, 575), title="Tabata Timer", reload=False)
