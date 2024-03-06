import vux
from vux.states import use_id


async def handler():
  md = use_id("paragraph", type="markdown")
  return [
    # tell Vux what to do after handler() is run
    md.set(
      md.content + "... unexpected '}' on line 42"
    )
  ]

with vux.page() as page:
  page.add(
    vux.Markdown(
      "Roses are red, violets are blue, ...",
      id="paragraph"
    )
  )
  page.add(
    vux.Button(fn=handler, "Continue")
  )

vux.launch()
