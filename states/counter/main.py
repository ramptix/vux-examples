# Simple button with a counter

import vux


async def on_click(count: int):
  # retrieve the state ($count)
  count += 1
  return { "count": count }

with vux.page() as page:
  page.add(
    vux.Button(
      fn=on_click,
      label="Click me! $count", # $count represents the value of the 'count' state
      count=0 # create a state
    )
  )

vux.launch()
