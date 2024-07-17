def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表 completed_models 中
    """
    while unprinted_designs:
        for unprinted_design in unprinted_designs:
            print(f"Printing model: {unprinted_design}")
            completed_models.append(unprinted_design)
            unprinted_designs.remove(unprinted_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
    