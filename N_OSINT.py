from colorama import init, Fore, Style

def generate_links(username):
    return {
        # Social media
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://facebook.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "YouTube": f"https://youtube.com/@{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}",
        "Twitter (X)": f"https://twitter.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "VK": f"https://vk.com/{username}",

        # Gaming
        "Xbox Live": f"https://account.xbox.com/en-us/profile?gamertag={username}",
        "Origin (EA)": f"https://www.origin.com/profiles/{username}",

        # Music / creative
        "SoundCloud": f"https://soundcloud.com/{username}",
        "Spotify (user)": f"https://open.spotify.com/user/{username}",
        "Bandcamp": f"https://{username}.bandcamp.com",

        # Professional
        "GitHub": f"https://github.com/{username}",
        "GitLab": f"https://gitlab.com/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Dev.to": f"https://dev.to/{username}",
    }

def main():
    init(autoreset=True)

    # Creator info
    creator_telegram = "https://t.me/nonstop4ek"  # <- Replace with actual username

    print(Fore.CYAN + Style.BRIGHT + "=== Social Link Generator ===")
    print(Fore.LIGHTBLUE_EX + f"👤 Created by: {creator_telegram}\n")

    username = input(Fore.YELLOW + "Enter your username: ").strip()
    if not username:
        print(Fore.RED + "❌ Name cannot be empty.")
        return

    links = generate_links(username)

    print(Fore.GREEN + "\nYour social/profile links:")
    for platform, url in links.items():
        print(Fore.MAGENTA + f"{platform}: " + Fore.WHITE + f"{url}")

    custom = input(Fore.YELLOW + "\nWould you like to add a custom link? (yes/no): ").strip().lower()
    if custom == "yes":
        custom_url = input("Enter your custom URL (include http/https): ").strip()
        if custom_url.startswith("http"):
            print(Fore.CYAN + f"✅ Your custom link: {custom_url}")
        else:
            print(Fore.RED + "❌ Invalid URL. It should start with http or https.")

if __name__ == "__main__":
    main()
