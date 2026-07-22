name: Build Flet APK

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Set up Java
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Install system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y libgtk-3-dev mesa-utils

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flet

      - name: Build APK with Flet
        run: |
          flet build apk --yes

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: app-apk
          path: build/apk/app-release.apk