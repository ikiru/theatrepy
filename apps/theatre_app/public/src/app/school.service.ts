import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class SchoolService {
  constructor(private _http: Http) {}

  show(school) {
    return this._http
      .post("/schools", school)
      .map(data => data.json())
      .toPromise();
  }
}
