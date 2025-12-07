import 'dart:convert';
import 'package:http/http.dart' as http;
import 'auth_service.dart';

class PostService {
  static const baseUrl = "http://127.0.0.1:8000/api/v1/posts";

  static Future<List<dynamic>> getPosts() async {
    final res = await http.get(
      Uri.parse(baseUrl),
      headers: {"Authorization": "Bearer ${AuthService.token}"},
    );

    return jsonDecode(res.body);
  }

  static Future<void> createPost(String title, String content) async {
    await http.post(
      Uri.parse(baseUrl),
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer ${AuthService.token}",
      },
      body: jsonEncode({"title": title, "content": content}),
    );
  }

  static Future<void> deletePost(String id) async {
    await http.delete(
      Uri.parse("$baseUrl/$id"),
      headers: {"Authorization": "Bearer ${AuthService.token}"},
    );
  }

  static Future<void> updatePost(
    String id,
    String? title,
    String? content,
  ) async {
    await http.put(
      Uri.parse("$baseUrl/$id"),
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer ${AuthService.token}",
      },
      body: jsonEncode({
        if (title != null) "title": title,
        if (content != null) "content": content,
      }),
    );
  }
}
