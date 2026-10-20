"""A Gradio demo, as its own quickstart writes it. Gradio reads GRADIO_SERVER_NAME and GRADIO_SERVER_PORT when launch()
is given neither, so the same file runs on a laptop and on a server."""
import gradio as gr


def greet(name, excited):
    greeting = f"Hello, {name or 'world'}"
    return greeting + ("!" if excited else ".")


demo = gr.Interface(
    fn=greet,
    inputs=[gr.Textbox(label="Your name"), gr.Checkbox(label="Excited")],
    outputs=gr.Textbox(label="Greeting"),
    title="Fast Deploy Gradio trial",
    description="A test service for Fast Deploy's Phase 20 live exercise. Not a real service.",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch()
