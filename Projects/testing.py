import colorama

# Initialize colorama
colorama.init()

# Print text in different colors
print(f"{colorama.Fore.RED}This text is red")
print(f"{colorama.Fore.GREEN}This text is green")
print(f"{colorama.Fore.BLUE}This text is blue")

# Reset colorama to default settings
colorama.deinit()


# Initialize colorama
colorama.init()

# Print text in different colors and styles
print(f"{colorama.Fore.RED}{colorama.Style.BRIGHT}Error: {colorama.Style.RESET_ALL}Something went wrong")
print(f"{colorama.Fore.YELLOW}Warning: {colorama.Style.RESET_ALL}This could be a problem")
print(f"{colorama.Fore.GREEN}Success: {colorama.Style.RESET_ALL}Everything is working fine")

# Reset colorama to default settings
colorama.deinit()
