const TelegramBot = require("node-telegram-bot-api");

// Ganti dengan token bot kamu
const token = "7505193327:AAH1V2BGos9Z-sWgNSJxBSy58f-Q-ZXF10A";

// Buat bot dengan polling
const bot = new TelegramBot(token, { polling: true });

// Command /start
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  bot.sendMessage(chatId, "Halo! Saya bot standar 🚀\nKetik sesuatu, nanti saya balas.");
});

// Echo semua pesan teks
bot.on("message", (msg) => {
  const chatId = msg.chat.id;
  if (msg.text && !msg.text.startsWith("/start")) {
    bot.sendMessage(chatId, `Kamu bilang: ${msg.text}`);
  }
});
