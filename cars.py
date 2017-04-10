makes = (
    (1, "Toyota"), (2, "Nissan"),
    (3, "Ford"), (4, "Mini"),
    (5, "Honda"), (6, "Dodge"),
)

models = (
    (1, "Altima", 2), (2, "Thunderbird", 3),
    (3, "Dart", 6), (4, "Accord", 5),
    (5, "Prius", 1), (6, "Countryman", 4),
    (7, "Camry", 1), (8, "F150", 3),
    (9, "Civic", 5), (10, "Ram", 6),
    (11, "Cooper", 4), (12, "Pilot", 5),
    (13, "Xterra", 2), (14, "Sentra", 2),
    (15, "Charger", 6)
)

colors = (
    (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
    (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
    (1, 1), (1, 2), (1, 7),
    (2, 1), (2, 3), (2, 7),
    (3, 2), (3, 3), (3, 7),
    (4, 3), (4, 5), (4, 8),
    (5, 2), (5, 4), (5, 8),
    (6, 2), (6, 6), (6, 7),
    (7, 1), (7, 3), (7, 7),
    (8, 1), (8, 5), (8, 8),
    (9, 1), (9, 6), (9, 7),
    (10, 2), (10, 5), (10, 7),
    (11, 3), (11, 6), (11, 8),
    (12, 1), (12, 4), (12, 7),
    (13, 2), (13, 6), (13, 8),
    (14, 2), (14, 5), (14, 8),
    (15, 1), (15, 4), (15, 7)
)

# stuff for string report(sr)
model_statement = ''
car_color_codes = []
car_color_names = ''

# stuff for dictionary report(dr)
model_report_dict = {}
make_models = {}

for make in makes:
    make_code = make[0]
    make_name = make[1]
    # sr
    print(make_name)
    print('--------------------')
    # dr
    model_report_dict[make_name] = {}

    for model in models:
        model_code = model[0]
        model_name = model[1]
        model_make_code = model[2]
        if model_make_code == make_code:
            # sr
            model_statement = model_name + ' available in '
            # dr
            make_models[model_name] = []

            for car in available_car_colors:
                car_code = car[0]
                car_color_code = car[1]
                if model_code == car_code:
                    car_color_codes.append(car_color_code)
            for color_code in car_color_codes:
                for color in colors:
                    model_color_code = color[0]
                    model_color_name = color[1]
                    if color_code == model_color_code:
                        # sr
                        car_color_names += model_color_name + ', '
                        # dr
                        make_models[model_name].append(model_color_name)
            # sr
            full_statement = model_statement + car_color_names
            print(full_statement[:-2])
            # dr
            model_report_dict[make_name].update(make_models)

            car_color_codes = []
            car_color_names = ''
        # sr
        model_statement = ''
        # dr
        make_models = {}
    # sr
    print('--------------------')
# dr
print(model_report_dict)

