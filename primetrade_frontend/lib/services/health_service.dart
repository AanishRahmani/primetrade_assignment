import 'dart:convert';
import 'package:http/http.dart' as http;

class HealthService {
  static const url = "http://127.0.0.1:8000/api/v1/health";

  static Future<Map<String, dynamic>> check() async {
    final res = await http.get(Uri.parse(url));
    return jsonDecode(res.body);
  }
}
