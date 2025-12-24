import gradio as gr
from incident_generator import generate_incident
from report_builder import build_report

def generate_incident_report():
    incident = generate_incident()
    return build_report(incident)

ui = gr.Interface(
    fn=generate_incident_report,
    inputs=[],
    outputs=gr.Markdown(),
    title="🚨 IncidentGPT – AI-Powered IT Incident Report Generator",
    description="""
    Generate enterprise-grade IT incident and postmortem reports
    similar to those used by SRE & DevOps teams.
    """
)

if __name__ == "__main__":
    ui.launch(share=True)
