import { Injectable } from "@angular/core";
import { Http } from "@angular/http";
import "rxjs";

@Injectable()
export class TechrolelistService {
  constructor(private _http: Http) {}

  createTechrolelist(techrolelist) {
    return this._http
      .post("/teechrolelist", techrolelist)
      .map(data => data.json())
      .toPromise();
  }
  getTechrolelist(techrolelist) {
    return this._http.get("/techrolelist").map(data => data.json()).toPromise();
  }
  updateTechrolelist(techrolelist) {
    return this._http
      .patch(`/techrolelist/${techrolelist._id}`, techrolelist)
      .map(data => data.json())
      .toPromise();
  }

  destroyTechrolelist(id: string) {
    return this._http
      .delete(`/techrolelist/${id}`)
      .map(data => data.json())
      .toPromise();
  }
}
