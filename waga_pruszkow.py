import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

# Пам'ять для вибору мови
user_lang = {}


# --- МЕНЮ УКРАЇНСЬКОЮ ---
def menu_ua():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📏 Про вагу", "📍 Локація")
    kb.add("💰 Тарифи", "🕒 Графік роботи")
    kb.add("🆕 Новини", "📞 Контакт")
    return kb


# --- МЕНЮ ПОЛЬСЬКОЮ ---
def menu_pl():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📏 O wadze", "📍 Lokalizacja")
    kb.add("💰 Cennik", "🕒 Godziny pracy")
    kb.add("🆕 Aktualności", "📞 Kontakt")
    return kb


# --- СТАРТ: ВИБІР МОВИ ---
@bot.message_handler(commands=["start"])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🇺🇦 Українська", "🇵🇱 Polski")

    bot.send_message(
        message.chat.id,
        "Оберіть мову / Wybierz język:",
        reply_markup=kb
    )


# --- ОБРОБКА ВИБОРУ МОВИ ---
@bot.message_handler(func=lambda m: m.text in ["🇺🇦 Українська", "🇵🇱 Polski"])
def set_language(message):
    chat_id = message.chat.id

    if message.text == "🇺🇦 Українська":
        user_lang[chat_id] = "ua"
        bot.send_message(chat_id, "Мову встановлено: 🇺🇦 Українська", reply_markup=menu_ua())

    elif message.text == "🇵🇱 Polski":
        user_lang[chat_id] = "pl"
        bot.send_message(chat_id, "Ustawiono język: 🇵🇱 Polski", reply_markup=menu_pl())


# --- ГОЛОВНА ЛОГІКА МЕНЮ ---
@bot.message_handler(func=lambda m: True)
def handle_menu(message):
    chat_id = message.chat.id
    lang = user_lang.get(chat_id)

    # Якщо мова ще не вибрана
    if not lang:
        return start(message)

    text = message.text

    # ----------------- УКРАЇНСЬКА -----------------
    if lang == "ua":

        if text == "📏 Про вагу":
            bot.send_message(chat_id,
                "📏 *Про вагу*\n\n"
                "Осьові ваги в Прушкові — точне зважування перед кордоном.\n\n"
                "На нашій сертифікованій станції ви можете виявити перегруз ще до кордону.\n"
                "Після зважування видаємо офіційний чек.\n\n"
                "Якщо є перегруз, можливе:\n"
                "• закриття T1 і відкриття нової\n"
                "• перевантаження вантажу в авто\n"
                "• перевертання контейнера\n\n"
                "Ваги сертифіковані, точність підтверджена документально.",
                parse_mode="Markdown"
            )

        elif text == "📍 Локація":
            bot.send_message(chat_id,
                "📍 *Адреса:*\n"
                "Przejazdowa 25, 05-800 Pruszków\n\n"
                "🗺️ Карта:\n"
                "https://maps.app.goo.gl/eMaghzH2Fj8KtG4v9",
                parse_mode="Markdown"
            )

        elif text == "💰 Тарифи":
            bot.send_message(chat_id,
                "💰 *Тарифи:*\n\n"
                "• Зважування однієї осі — 30 zł\n"
                "• Повне зважування авто + квитанція (до 5 осей) — 150 zł",
                parse_mode="Markdown"
            )

        elif text == "🕒 Графік роботи":
            bot.send_message(chat_id,
                "🕒 *Графік роботи:*\n\n"
                "Пн–Пт: 08:00–16:00\n"
                "Сб: за погодженням\n"
                "Нд: за погодженням\n\n"
                "Можливий індивідуальний графік за погодженням.",
                parse_mode="Markdown"
            )

        elif text == "🆕 Новини":
            bot.send_message(chat_id, "🆕 Новини:\nТут будуть публікуватися важливі оновлення.")

        elif text == "📞 Контакт":
            bot.send_message(chat_id,
                "📞 *Контакт:*\n\n"
                "Telegram: @waga_pruszkow\n"
                "Телефон: +48 795 314 410",
                parse_mode="Markdown"
            )

        else:
            bot.send_message(chat_id, "Оберіть пункт меню 👇", reply_markup=menu_ua())


    # ----------------- ПОЛЬСЬКА -----------------
    elif lang == "pl":

        if text == "📏 O wadze":
            bot.send_message(chat_id,
                "📏 *O wadze*\n\n"
                "Wagi osiowe w Pruszkowie — dokładne ważenie przed granicą.\n\n"
                "Na naszej certyfikowanej stacji możesz sprawdzić przeciążenie przed granicą.\n"
                "Po ważeniu wydajemy oficjalny paragon.\n\n"
                "W przypadku przeciążenia możliwe jest:\n"
                "• zamknięcie T1 i otwarcie nowego\n"
                "• przeładunek towaru do innego pojazdu\n"
                "• obracanie kontenera\n\n"
                "Wagi są certyfikowane, dokładność potwierdzona dokumentami.",
                parse_mode="Markdown"
            )

        elif text == "📍 Lokalizacja":
            bot.send_message(chat_id,
                "📍 *Adres:*\n"
                "Przejazdowa 25, 05-800 Pruszków\n\n"
                "🗺️ Mapa:\n"
                "https://maps.app.goo.gl/eMaghzH2Fj8KtG4v9",
                parse_mode="Markdown"
            )

        elif text == "💰 Cennik":
            bot.send_message(chat_id,
                "💰 *Cennik:*\n\n"
                "• Ważenie jednej osi — 30 zł\n"
                "• Pełne ważenie pojazdu + paragon (do 5 osi) — 150 zł",
                parse_mode="Markdown"
            )

        elif text == "🕒 Godziny pracy":
            bot.send_message(chat_id,
                "🕒 *Godziny pracy:*\n\n"
                "Pon–Pt: 08:00–16:00\n"
                "Sob: według ustaleń\n"
                "Ndz: według ustaleń\n\n"
                "Możliwy indywidualny harmonogram po uzgodnieniu.",
                parse_mode="Markdown"
            )

        elif text == "🆕 Aktualności":
            bot.send_message(chat_id, "🆕 Aktualności:\nWażne informacje będą publikowane tutaj.")

        elif text == "📞 Kontakt":
            bot.send_message(chat_id,
                "📞 *Kontakt:*\n\n"
                "Telegram: @waga_pruszkow\n"
                "Telefon: +48 795 314 410",
                parse_mode="Markdown"
            )

        else:
            bot.send_message(chat_id, "Wybierz opcję z menu 👇", reply_markup=menu_pl())


if __name__ == "__main__":
    bot.infinity_polling()
