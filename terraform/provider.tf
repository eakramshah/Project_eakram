terraform {
  required_providers {
    spotify = {
      source = "conradludgate/spotify"
      version = "0.2.7"
    }
  }
}

provider "spotify" {
  # Configuration options
  api_key = "EdlbkO11E2DkDRC89_xWFjOK-Gt5XzUvTVuEj1tQkcV-yNkMrVQ7SWgpv5cfz_0g"
}