// A small Express service that listens on a fixed port, as many tutorials do; it never reads PORT.
const express = require("express");

const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.json({ service: "node-port", trial: "Fast Deploy Phase 20", node: process.version, port });
});

app.get("/health", (req, res) => {
  res.json({ ok: true });
});

const server = app.listen(port, () => {
  console.log(`node-port listening on port ${port}`);
});

process.on("SIGTERM", () => {
  server.close(() => process.exit(0));
});
