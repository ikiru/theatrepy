import { Component, OnInit } from "@angular/core";
import { OAuthService } from "../../../src/oauth-service";

@Component({
  selector: "app-home",
  templateUrl: "./home.component.html",
  styleUrls: ["./home.component.css"]
})
export class HomeComponent implements OnInit {
  constructor(private oAuthService: OAuthService) {}

  public login() {
    this.oAuthService.initImplicitFlow();
  }

  public logoff() {
    this.oAuthService.logOut();
  }

  public get name() {
    let claims = this.oAuthService.getIdentityClaims();
    if (!claims) return null;
    return claims.given_name;
  }
  ngOnInit() {}
}
