import 'package:flutter/material.dart';
import 'package:primetrade_frontend/pages/dsahboard_page.dart';
import '../services/auth_service.dart';
import 'register_page.dart';

class LoginPage extends StatefulWidget {
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final email = TextEditingController();
  final password = TextEditingController();

  String error = "";

  login() async {
    final res = await AuthService.login(email.text, password.text);

    if (AuthService.token != null) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DashboardPage()),
      );
    } else {
      setState(() => error = res["detail"] ?? "Login failed");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: SizedBox(
          width: 350,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              TextField(
                controller: email,
                decoration: InputDecoration(labelText: "email"),
              ),
              TextField(
                controller: password,
                decoration: InputDecoration(labelText: "Password"),
                obscureText: true,
              ),
              SizedBox(height: 20),
              ElevatedButton(onPressed: login, child: Text("Login")),
              TextButton(
                onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => RegisterPage()),
                ),
                child: Text("Create an account"),
              ),
              Text(error, style: TextStyle(color: Colors.red)),
            ],
          ),
        ),
      ),
    );
  }
}
