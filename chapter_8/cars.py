def cars(manufact, model, **items):
    car_dict = {
        'manufactiurer': manufact.title(),
        'model': model.title(),
    }
    for key, value in items.items():
        car_dict[key] = value
    return car_dict


