import 'package:flutter/material.dart';
import '../services/auth_service.dart';
import 'login_page.dart';

class RegisterPage extends StatefulWidget {
  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  final username = TextEditingController();
  final email = TextEditingController();
  final password = TextEditingController();

  String message = "";

  register() async {
    final res = await AuthService.register(
      username.text,
      email.text,
      password.text,
    );

    setState(() => message = res.toString());
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
                controller: username,
                decoration: InputDecoration(labelText: "Username"),
              ),
              TextField(
                controller: email,
                decoration: InputDecoration(labelText: "Email"),
              ),
              TextField(
                controller: password,
                decoration: InputDecoration(labelText: "Password"),
                obscureText: true,
              ),
              SizedBox(height: 20),
              ElevatedButton(onPressed: register, child: Text("Register")),
              TextButton(
                onPressed: () => Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => LoginPage()),
                ),
                child: Text("Back to login"),
              ),
              Text(message),
            ],
          ),
        ),
      ),
    );
  }
}
