def years_to_days(years):
    days = years * 360
    return days

def days_to_hours(days):
    hours = days * 24
    return hours

def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes

def minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds

ask_in_years = int(input("How many years?\n"))
days = years_to_days(ask_in_years)
hours = days_to_hours(days)
minutes = hours_to_minutes(hours)
seconds = minutes_to_seconds(minutes)

print(f"\n\n{ask_in_years} years transform into {seconds} seconds!")
