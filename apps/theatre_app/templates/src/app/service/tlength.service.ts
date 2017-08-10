import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class TlengthService {
  constructor(private _http: Http) {}

  createTlength(tlength) {
    return this._http
      .post("/tlength", tlength)
      .map(data => data.json())
      .toPromise();
  }
  getTlength(tlength) {
    return this._http.get("/tlength").map(data => data.json()).toPromise();
  }
}
