from datetime import datetime

# Memoization cache for days_between function
days_between_cache = {}


def days_between(start_date_str, end_date_str):
    """Calculate the number of days between two dates."""
    if (start_date_str, end_date_str) in days_between_cache:
        return days_between_cache[(start_date_str, end_date_str)]

    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    delta = end_date - start_date

    # Cache the result
    days_between_cache[(start_date_str, end_date_str)] = delta.days
    return delta.days


# Memoization cache for compound_interest function
compound_interest_cache = {}


def compound_interest(initial_capital, growth_rate, reset_period):
    """Calculate compound interest."""
    if (initial_capital, growth_rate, reset_period) in compound_interest_cache:
        return compound_interest_cache[(initial_capital, growth_rate, reset_period)]

    if reset_period <= 0:
        return 0

    final_capital = initial_capital * ((1 + growth_rate) ** reset_period)

    # Cache the result
    compound_interest_cache[(initial_capital, growth_rate,
                             reset_period)] = final_capital
    return final_capital


def main():
    currency = input("Enter the currency symbol: ")
    initial_capital = float(input("Enter your initial capital: "))
    growth_rate = float(input("Enter the growth rate (in decimal): "))
    reset_period = int(input("Enter the reset period in days: "))

    start_date_str = input("When will/did you start? (YYYY-MM-DD): ")
    end_date_str = input("When will the investment mature? (YYYY-MM-DD): ")

    num_days = days_between(start_date_str, end_date_str)
    print("Investment period:", num_days)

    base_reps, extra_days = divmod(num_days, reset_period)
    print("Base repetitions:", base_reps)
    print("Extra days:", extra_days)

    final_amount = compound_interest(
        initial_capital, growth_rate, reset_period)

    base_return = base_reps * final_amount
    extra_return = compound_interest(initial_capital, growth_rate, extra_days)

    final_return = base_return + extra_return

    # Format final return with currency formatting for values above 1000
    formatted_final_return = "{:,.2f} {}".format(final_return, currency) if abs(final_return) >= 1000 \
                             else "{:.2f} {}".format(final_return, currency)

    print("Final return:", formatted_final_return)


if __name__ == "__main__":
    main()
