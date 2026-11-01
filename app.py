
import gradio as gr

def prepare_video(mode, prompt, image, quality, ratio, duration):
    if not prompt.strip():
        return "कृपया पहले Video Prompt लिखें।"

    if mode == "Image to Video" and image is None:
        return "कृपया एक Image Upload करें।"

    return (
        "आपकी Video Settings तैयार हैं!\n\n"
        f"Mode: {mode}\n"
        f"Quality: {quality}\n"
        f"Ratio: {ratio}\n"
        f"Duration: {duration}\n\n"
        "AI Model अभी Connect नहीं हुआ है। "
        "अगले चरण में Free AI Model जोड़ेंगे।"
    )

with gr.Blocks(title="Wonder AI Studio") as demo:
    gr.Markdown("# 🎬 Wonder AI Studio")
    gr.Markdown("Free AI Video Generator")

    mode = gr.Radio(
        ["Text to Video", "Image to Video"],
        value="Text to Video",
        label="Generation Mode"
    )

    prompt = gr.Textbox(
        label="Video Prompt",
        placeholder="Describe your video...",
        lines=4
    )

    image = gr.Image(
        type="filepath",
        label="Upload Image"
    )

    quality = gr.Dropdown(
        ["720p HD"],
        value="720p HD",
        label="Quality"
    )

    ratio = gr.Dropdown(
        ["9:16 Shorts", "16:9 Long Video"],
        value="9:16 Shorts",
        label="Aspect Ratio"
    )

    duration = gr.Dropdown(
        ["5 Seconds", "10 Seconds"],
        value="5 Seconds",
        label="Duration"
    )

    generate = gr.Button("Generate Video")
    result = gr.Textbox(label="Status")

    generate.click(
        prepare_video,
        inputs=[mode, prompt, image, quality, ratio, duration],
        outputs=result
    )

demo.launch()
