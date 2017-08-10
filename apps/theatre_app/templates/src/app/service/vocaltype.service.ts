import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class VocaltypeService {
  constructor(private _http: Http) {}

  createVocaltype(vocaltype) {
    return this._http
      .post("/vocaltype", vocaltype)
      .map(data => data.json())
      .toPromise();
  }
  getVocaltype(vocaltype) {
    return this._http.get("/vocaltype").map(data => data.json()).toPromise();
  }
  updateVocaltype(vocaltype) {
    return this._http
      .patch(`/vocaltype/${vocaltype._id}`, vocaltype)
      .map(data => data.json())
      .toPromise();
  }

  destroyVocaltype(id: string) {
    return this._http
      .delete(`/vocaltype/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
