import 'package:flutter/material.dart';
import 'package:primetrade_frontend/services/health_service.dart';
import '../services/post_service.dart';
import 'edit_post_page.dart';

class DashboardPage extends StatefulWidget {
  @override
  State<DashboardPage> createState() => _DashboardPageState();
}

class _DashboardPageState extends State<DashboardPage> {
  List posts = [];
  String status = "Checking...";

  final titleCtrl = TextEditingController();
  final contentCtrl = TextEditingController();

Future<void> load() async {
  final newPosts = await PostService.getPosts();
  final health = await HealthService.check();

  setState(() {
    posts = newPosts;
    status = health["status"];
  });
}


  createPost() async {
    await PostService.createPost(titleCtrl.text, contentCtrl.text);
    titleCtrl.clear();
    contentCtrl.clear();
    load();
  }

  @override
  void initState() {
    super.initState();
    load();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Dashboard | Server: $status")),
      body: Padding(
        padding: EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(
              controller: titleCtrl,
              decoration: InputDecoration(labelText: "Title"),
            ),
            TextField(
              controller: contentCtrl,
              decoration: InputDecoration(labelText: "Content"),
            ),
            ElevatedButton(onPressed: createPost, child: Text("Create Post")),
            SizedBox(height: 20),
            Expanded(
              child: ListView(
                children: posts.map((p) {
                  return Card(
                    child: ListTile(
                      title: Text(p["title"]),
                      subtitle: Text(p["content"]),
                      trailing: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          IconButton(
                            icon: Icon(Icons.edit),
                            onPressed: () => Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (_) => EditPostPage(post: p),
                              ),
                            ),
                          ),
                          IconButton(
                            icon: Icon(Icons.delete),
                            onPressed: () async {
                              await PostService.deletePost(p["id"]);
                              load();
                            },
                          ),
                        ],
                      ),
                    ),
                  );
                }).toList(),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
