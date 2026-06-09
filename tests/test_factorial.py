import pytest
from playwright.sync_api import Page, expect
    
def test_calcular_factorial_numero_entero_positivo (page: Page):
    print("Given la persona usuaria visita la pagina de Factorial")
    page.goto("https://qainterview.pythonanywhere.com/")
    print("When introduce un numero entero positivo")
    page.get_by_role("textbox", name="Enter an integer").fill("3")
    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()
    print("Then debe ver el resultado del factorial del numero esperado")
    expect(page.locator("#resultDiv")).to_contain_text("6")

def test_calcular_factorial_valor_nonumerico (page: Page): 
    print("Given la persona usuaria visita la pagina de Factorial")  
    page.goto("https://qainterview.pythonanywhere.com/")
    print("When introduce un valor de texto")
    page.get_by_role("textbox", name="Enter an integer").fill("texto")
    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()
    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("Please enter an integer")).to_be_visible()

#Se desactiva test porque genera error https://adalabequipo4.atlassian.net/browse/PF-2
@pytest.mark.xfail(reason="Bug PF-2 pendiente de resolver") 
def test_calcular_factorial_valor_negativo (page: Page):
    print("Given la persona usuaria visita la pagina de Factorial")
    page.goto("https://qainterview.pythonanywhere.com/")
    print("When introduce un valor numero negativo")
    page.get_by_role("textbox", name="Enter an integer").fill("-1")
    print("And hace click en calcular")
    page.get_by_role("button", name="Calculate!").click()
    print("Then debe ver un mensaje de error")
    expect(page.get_by_text("Please enter an integer")).to_be_visible()

