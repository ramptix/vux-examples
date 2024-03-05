import vux
from vux.hooks import use_local_storage


async def get_storage():
  storage = use_local_storage()
  print(storage.data) # print on our side

async def set_storage():
  storage = use_local_storage()
  return {
    "label": "Set!",
    "procedure": [
      # after this render, execute:
      storage.set_item("hello", "world")
    ]
  }

with vux.page() as page:
  page.add(
    vux.Button(fn=get_storage, label="Log storage")
  )
  page.add(
    vux.Button(fn=set_storage, label="Set storage")
  )

vux.launch()
