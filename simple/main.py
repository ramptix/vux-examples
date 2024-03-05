# Minimal Vux example with Markdown & a form

import vux


async def hello_world(name: str, intensity: int = 1):
  return "Hello " * intensity + name

with vux.page() as page:
  page.add("# Vux Form")
  page.form(fn=hello_world)

vux.launch()
