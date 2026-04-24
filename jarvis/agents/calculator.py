"""Agent pour les calculs mathématiques"""
from sympy import symbols, diff, integrate, simplify, solve, sqrt, pi, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import re
from typing import Dict

class Calculator:
    """Effectue des calculs mathématiques"""
    
    def __init__(self):
        self.x = symbols('x')
        self.transformations = (standard_transformations + (implicit_multiplication_application,))
    
    def calculate(self, expression: str) -> Dict[str, str]:
        """Évalue une expression mathématique"""
        try:
            # Remplace les symboles courants
            expression = expression.replace("π", "pi")
            expression = expression.replace("e", "E")
            
            expr = parse_expr(expression, transformations=self.transformations)
            result = expr
            
            return {
                "success": True,
                "expression": str(expr),
                "result": str(result),
                "decimal": float(result) if result.is_number else None
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def derivative(self, expression: str, variable: str = "x") -> Dict[str, str]:
        """Calcule la dérivée"""
        try:
            var = symbols(variable)
            expr = parse_expr(expression, transformations=self.transformations, local_dict={variable: var})
            derivative_result = diff(expr, var)
            
            return {
                "success": True,
                "expression": str(expr),
                "derivative": str(derivative_result),
                "simplified": str(simplify(derivative_result))
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def integral(self, expression: str, variable: str = "x") -> Dict[str, str]:
        """Calcule l'intégrale"""
        try:
            var = symbols(variable)
            expr = parse_expr(expression, transformations=self.transformations, local_dict={variable: var})
            integral_result = integrate(expr, var)
            
            return {
                "success": True,
                "expression": str(expr),
                "integral": str(integral_result),
                "simplified": str(simplify(integral_result))
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def solve_equation(self, equation: str, variable: str = "x") -> Dict[str, str]:
        """Résout une équation"""
        try:
            # Format: "x^2 + 2*x - 3 = 0" ou "x^2 + 2*x - 3"
            if "=" in equation:
                left, right = equation.split("=")
                equation = f"({left}) - ({right})"
            
            var = symbols(variable)
            expr = parse_expr(equation, transformations=self.transformations, local_dict={variable: var})
            solutions = solve(expr, var)
            
            return {
                "success": True,
                "equation": str(expr),
                "solutions": str(solutions),
                "count": len(solutions)
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
