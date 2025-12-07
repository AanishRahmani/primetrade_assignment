import 'dart:convert';
import 'package:http/http.dart' as http;

class AuthService {
  static const baseUrl = "http://127.0.0.1:8000/api/v1/auth";
  static String? token;


static Future<Map<String, dynamic>> login(String email, String password) async {
  final res = await http.post(
    Uri.parse("$baseUrl/login"),
    headers: {"Content-Type": "application/json"},
    body: jsonEncode({
      "email": email,
      "password": password,
    }),
  );

  final data = jsonDecode(res.body);

  if (res.statusCode == 200) {
    token = data["access_token"];
  }

  return data;
}


    static Future<Map<String, dynamic>> register(
      String username, String email, String password) async {
    final res = await http.post(
      Uri.parse("$baseUrl/register"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "username": username,
        "email": email,
        "password": password,
      }),
    );

    return jsonDecode(res.body);
  }
}
