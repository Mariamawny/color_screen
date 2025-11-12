import 'package:flutter/material.dart';

class ColorScreen extends StatelessWidget {
   ColorScreen(this.ScreenColor,{super.key});
Color ScreenColor;
  @override
  Widget build(BuildContext context) {
    return Container(
      color: ScreenColor,
      
    );
  }
}