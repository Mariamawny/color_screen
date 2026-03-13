// ignore_for_file: must_be_immutable, non_constant_identifier_names

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




