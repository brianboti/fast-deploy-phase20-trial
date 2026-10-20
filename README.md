# Fast Deploy Phase 20 trial

Test fixtures for Fast Deploy's Phase 20 live exercise ("read more, refuse less", platform 1.22.0): four small web
services in folders, each written the way a developer would write it for a tutorial, with nothing added for the
platform. Not real services. The platform reads each folder as it is and drafts its contract; a person's merge of the
contract pull request is the review.

| Folder | What it exercises |
|---|---|
| `gradio-hello/` | A Gradio app with no application object the reader knows: `gradio` among the dependencies decides the start (`python app.py` with `GRADIO_SERVER_NAME` and `GRADIO_SERVER_PORT`) |
| `aiohttp-main/` | An aiohttp app whose `main()` builds the application and calls `web.run_app`: the last rung, `python main.py`, with `HOST` and `PORT` set |
| `node-port/` | An Express service that listens on the literal port 3000 and never reads `PORT`; `.nvmrc` asks for Node.js 18, a line at its end of life |
| `django-static/` | A Django project whose `requirements.txt` includes `requirements/base.txt`, with static files for `collectstatic` and migrations for `migrate`; `.python-version` asks for Python 3.10, a line at its end of life |

"Deploy everything in this repository" (`onboard_application` with `all=true`) opens one contract pull request per folder.
