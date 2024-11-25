from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Função para responder ao comando /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🎉 Olá! Bem-vindo ao bot oficial da *Festa MC - 5 anos*! 🎈\n"
        "Aqui estão os comandos disponíveis:\n"
        "- /info: Detalhes sobre a festa\n"
        "- /local: Endereço do evento\n"
        "- /horario: Horário da festa\n"
        "- /confirmar: Confirme sua presença."
    )

# Função para fornecer detalhes sobre a festa
def info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🎊 A festa será no dia *10/12*, às *18h*, com o tema: *Noite de Gala*.\n"
        "Venha preparado(a) para uma noite inesquecível! 💃🕺"
    )

# Função para fornecer o endereço
def local(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "📍 *Endereço do Evento:*\n"
        "Salão de Festas XYZ\n"
        "Rua das Flores, 123, Centro, Cidade."
    )

# Função para fornecer o horário
def horario(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "⏰ *Horário da Festa:*\n"
        "A festa começa às 18h e termina à meia-noite."
    )

# Função para confirmação de presença
def confirmar(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🎉 Obrigado por confirmar sua presença! Por favor, envie seu nome completo para registrar a confirmação. 😊"
    )

# Função para mensagens não reconhecidas
def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("❓ Desculpe, não entendi. Por favor, use um dos comandos disponíveis.")

def main():
    # Substituído pelo token do seu bot fornecido pelo BotFather
    updater = Updater("7074333923:AAFpfxXmkyTvNJZxMS2ekvHOh275_X7M0gI")
    dispatcher = updater.dispatcher

    # Adicionando comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("local", local))
    dispatcher.add_handler(CommandHandler("horario", horario))
    dispatcher.add_handler(CommandHandler("confirmar", confirmar))

    # Adicionando mensagens desconhecidas
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    # Inicia o bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()