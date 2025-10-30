def car(manufacturer,model,**info):
  manufacturer = manufacturer.title()
  model = model.title()
  info['manufacturer'] = manufacturer
  info['model'] = model

  print(info)

car('ferrari', 'SF70', color = 'red', chassis='air drawn')