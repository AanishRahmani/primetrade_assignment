import 'package:flutter/material.dart';
import '../services/post_service.dart';

class EditPostPage extends StatefulWidget {
  final Map post;
  EditPostPage({required this.post});

  @override
  State<EditPostPage> createState() => _EditPostPageState();
}

class _EditPostPageState extends State<EditPostPage> {
  late TextEditingController titleCtrl;
  late TextEditingController contentCtrl;

  @override
  void initState() {
    super.initState();
    titleCtrl = TextEditingController(text: widget.post["title"]);
    contentCtrl = TextEditingController(text: widget.post["content"]);
  }

  updatePost() async {
    await PostService.updatePost(
      widget.post["id"],
      titleCtrl.text,
      contentCtrl.text,
    );

    Navigator.pop(context);
  }

  @override
  Widget build(BuildContext contexte) {
    return Scaffold(
      appBar: AppBar(title: Text("Edit Post")),
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
            ElevatedButton(onPressed: updatePost, child: Text("Save")),
          ],
        ),
      ),
    );
  }
}
