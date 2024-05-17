import allure


def layer(name):
    return allure.label("layer", name)


def feature(name):
    return allure.label("feature", name)