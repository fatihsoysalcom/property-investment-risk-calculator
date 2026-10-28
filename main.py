import sys

def calculate_rental_yield(
    purchase_price,
    monthly_rent_expected,
    initial_acquisition_costs_percent,
    loan_amount_percent,
    loan_interest_rate_annual,
    vacancy_months_per_year,
    maintenance_repair_percent_of_rent,
    management_fees_percent_of_rent,
    property_tax_percent_of_value
):
    """
    Calculates the net annual rental yield considering various costs.
    """
    annual_rent_gross = monthly_rent_expected * 12

    # --- Initial Investment Costs ---
    initial_acquisition_costs = purchase_price * initial_acquisition_costs_percent
    total_initial_investment = purchase_price + initial_acquisition_costs

    # --- Annual Loan Interest Cost (Simplified) ---
    # This assumes a fixed interest payment on the principal amount for the year.
    # A full amortization schedule is beyond the scope of this simple example.
    loan_principal = purchase_price * loan_amount_percent
    annual_loan_interest_cost = loan_principal * loan_interest_rate_annual

    # --- Annual Operating Expenses ---
    # Article concept: accounting for vacancy periods
    vacancy_loss = (monthly_rent_expected * vacancy_months_per_year)
    # Article concept: accounting for maintenance/repair costs
    maintenance_repair_cost = annual_rent_gross * maintenance_repair_percent_of_rent
    # Article concept: accounting for management fees
    management_fees_cost = annual_rent_gross * management_fees_percent_of_rent
    # Article concept: accounting for property taxes
    property_tax_cost = purchase_price * property_tax_percent_of_value

    total_annual_operating_expenses = (
        vacancy_loss
        + maintenance_repair_cost
        + management_fees_cost
        + property_tax_cost
    )
    # Article concept: loan interest as a significant annual cost
    total_annual_expenses_with_loan = total_annual_operating_expenses + annual_loan_interest_cost

    net_annual_income = annual_rent_gross - total_annual_expenses_with_loan
    net_annual_yield = (net_annual_income / total_initial_investment) * 100 if total_initial_investment > 0 else 0

    return {
        "annual_rent_gross": annual_rent_gross,
        "initial_acquisition_costs": initial_acquisition_costs,
        "total_initial_investment": total_initial_investment,
        "annual_loan_interest_cost": annual_loan_interest_cost,
        "vacancy_loss": vacancy_loss,
        "maintenance_repair_cost": maintenance_repair_cost,
        "management_fees_cost": management_fees_cost,
        "property_tax_cost": property_tax_cost,
        "total_annual_operating_expenses": total_annual_operating_expenses,
        "total_annual_expenses_with_loan": total_annual_expenses_with_loan,
        "net_annual_income": net_annual_income,
        "net_annual_yield": net_annual_yield
    }

def print_results(title, results):
    print(f"\n--- {title} ---")
    print(f"  Gross Annual Rent: {results['annual_rent_gross']:.2f}")
    print(f"  Initial Acquisition Costs: {results['initial_acquisition_costs']:.2f}")
    print(f"  Total Initial Investment: {results['total_initial_investment']:.2f}")
    print(f"  --- Annual Expenses ---")
    print(f"    Loan Interest Cost: {results['annual_loan_interest_cost']:.2f}")
    print(f"    Vacancy Loss: {results['vacancy_loss']:.2f}")
    print(f"    Maintenance/Repair: {results['maintenance_repair_cost']:.2f}")
    print(f"    Management Fees: {results['management_fees_cost']:.2f}")
    print(f"    Property Tax: {results['property_tax_cost']:.2f}")
    print(f"  Total Annual Expenses: {results['total_annual_expenses_with_loan']:.2f}")
    print(f"  Net Annual Income: {results['net_annual_income']:.2f}")
    print(f"  Net Annual Yield: {results['net_annual_yield']:.2f}%")
    if results['net_annual_yield'] < 0:
        # Article concept: highlighting potential loss scenarios
        print("  WARNING: This scenario results in a negative net annual yield (loss).")

if __name__ == "__main__":
    print("Kira Getirisi Hesaplayıcısı: Zarar Senaryolarını Göstermenin Önemi")
    print("------------------------------------------------------------------")
    print("This calculator demonstrates how various costs impact rental yield,")
    print("showing optimistic vs. pessimistic scenarios.")

    # --- User-definable Base Inputs ---
    # These values can be changed by the user to simulate different properties.
    purchase_price = 500000.0  # Property purchase price (e.g., 500,000 TL)
    monthly_rent_expected = 5000.0 # Expected monthly rental income (e.g., 5,000 TL)
    initial_acquisition_costs_percent = 0.03 # e.g., 3% for stamp duty, agent fees
    loan_amount_percent = 0.50 # e.g., 50% of purchase price financed
    loan_interest_rate_annual = 0.15 # e.g., 15% annual interest rate (simplified)

    print(f"\nBase Inputs:")
    print(f"  Purchase Price: {purchase_price:.2f}")
    print(f"  Expected Monthly Rent: {monthly_rent_expected:.2f}")
    print(f"  Initial Acquisition Costs: {initial_acquisition_costs_percent*100:.1f}% of price")
    print(f"  Loan Amount: {loan_amount_percent*100:.1f}% of price")
    print(f"  Annual Loan Interest Rate: {loan_interest_rate_annual*100:.1f}%")

    # --- Optimistic Scenario Parameters ---
    # Minimal vacancy, low maintenance, low management fees, standard property tax.
    vacancy_months_optimistic = 0.5 # Half a month vacant per year
    maintenance_repair_percent_optimistic = 0.005 # 0.5% of annual rent
    management_fees_percent_optimistic = 0.05 # 5% of annual rent
    property_tax_percent_optimistic = 0.001 # 0.1% of property value

    # --- Pessimistic Scenario Parameters ---
    # Higher vacancy, higher maintenance, higher management fees, higher property tax.
    # This scenario highlights potential loss.
    vacancy_months_pessimistic = 2.0 # Two months vacant per year
    maintenance_repair_percent_pessimistic = 0.02 # 2% of annual rent
    management_fees_percent_pessimistic = 0.10 # 10% of annual rent
    property_tax_percent_pessimistic = 0.002 # 0.2% of property value (e.g., higher municipality tax)

    # Calculate and print for Optimistic Scenario
    optimistic_results = calculate_rental_yield(
        purchase_price,
        monthly_rent_expected,
        initial_acquisition_costs_percent,
        loan_amount_percent,
        loan_interest_rate_annual,
        vacancy_months_optimistic,
        maintenance_repair_percent_optimistic,
        management_fees_percent_optimistic,
        property_tax_percent_optimistic
    )
    print_results("Optimistic Scenario", optimistic_results)

    # Calculate and print for Pessimistic Scenario
    pessimistic_results = calculate_rental_yield(
        purchase_price,
        monthly_rent_expected,
        initial_acquisition_costs_percent,
        loan_amount_percent,
        loan_interest_rate_annual,
        vacancy_months_pessimistic,
        maintenance_repair_percent_pessimistic,
        management_fees_percent_pessimistic,
        property_tax_percent_pessimistic
    )
    print_results("Pessimistic Scenario (Loss Scenario Emphasis)", pessimistic_results)

    print("\nNote: This is a simplified model. Real-world scenarios may involve")
    print("more complex calculations (e.g., full loan amortization, inflation,")
    print("property value appreciation/depreciation, fluctuating interest rates).")
